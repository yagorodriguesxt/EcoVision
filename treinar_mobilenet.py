
from pathlib import Path
import json

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

DATASET = Path("dataset")
IMG_SIZE = (160, 160)
BATCH_SIZE = 16
SEED = 42
EPOCHS_INICIAIS = 8
EPOCHS_FINE_TUNING = 5

TRAIN_DIR = DATASET / "train"
VAL_DIR = DATASET / "validation"
MODELO_DIR = Path("modelos")
RESULTADOS_DIR = Path("resultados")


def carregar_dados(diretorio, shuffle):
    return keras.utils.image_dataset_from_directory(
        diretorio,
        image_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        seed=SEED,
        shuffle=shuffle,
    )


def criar_mobilenet(numero_classes):
    aumento = keras.Sequential([
        layers.RandomFlip("horizontal"),
        layers.RandomRotation(0.1),
        layers.RandomZoom(0.1),
    ], name="aumento_dados")

    base = keras.applications.MobileNetV2(
        input_shape=(*IMG_SIZE, 3),
        include_top=False,
        weights="imagenet",
    )
    base.trainable = False

    entradas = keras.Input(shape=(*IMG_SIZE, 3))
    x = aumento(entradas)
    x = layers.Rescaling(1.0 / 127.5, offset=-1)(x)
    x = base(x, training=False)
    x = layers.GlobalAveragePooling2D()(x)
    x = layers.Dropout(0.25)(x)
    saidas = layers.Dense(numero_classes, activation="softmax")(x)

    modelo = keras.Model(entradas, saidas)
    return modelo, base


def compilar(modelo, taxa_aprendizado):
    modelo.compile(
        optimizer=keras.optimizers.Adam(
            learning_rate=taxa_aprendizado
        ),
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"],
    )


def main():
    if not TRAIN_DIR.is_dir() or not VAL_DIR.is_dir():
        raise FileNotFoundError(
            "Prepare dataset/train e dataset/validation."
        )

    treino = carregar_dados(TRAIN_DIR, shuffle=True)
    validacao = carregar_dados(VAL_DIR, shuffle=False)

    classes = treino.class_names
    if len(classes) != 3:
        raise ValueError(f"Esperadas 3 classes, encontradas: {classes}")

    if classes != validacao.class_names:
        raise ValueError("As classes de treino e validação não coincidem.")

    print("Ordem das classes:", classes)

    modelo, base = criar_mobilenet(len(classes))

    compilar(modelo, 1e-3)

    callbacks = [
        keras.callbacks.EarlyStopping(
            monitor="val_loss",
            patience=3,
            restore_best_weights=True,
        )
    ]

    historico_inicial = modelo.fit(
        treino,
        validation_data=validacao,
        epochs=EPOCHS_INICIAIS,
        callbacks=callbacks,
    )

    # Descongela as camadas finais para ajuste fino.
    base.trainable = True

    for camada in base.layers[:-30]:
        camada.trainable = False

    # Mantém BatchNormalization congelada para maior estabilidade.
    for camada in base.layers:
        if isinstance(camada, layers.BatchNormalization):
            camada.trainable = False

    compilar(modelo, 1e-5)

    callbacks_fine = [
        keras.callbacks.EarlyStopping(
            monitor="val_loss",
            patience=3,
            restore_best_weights=True,
        )
    ]

    historico_fine = modelo.fit(
        treino,
        validation_data=validacao,
        epochs=EPOCHS_FINE_TUNING,
        callbacks=callbacks_fine,
    )

    MODELO_DIR.mkdir(parents=True, exist_ok=True)
    RESULTADOS_DIR.mkdir(parents=True, exist_ok=True)

    modelo.save(MODELO_DIR / "ecovision_mobilenetv2.keras")

    (RESULTADOS_DIR / "classes.json").write_text(
        json.dumps(classes, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    historico_completo = {
        "treinamento_inicial": historico_inicial.history,
        "fine_tuning": historico_fine.history,
    }

    (RESULTADOS_DIR / "historico_mobilenetv2.json").write_text(
        json.dumps(historico_completo, indent=2),
        encoding="utf-8",
    )

    print(
        "Modelo salvo em modelos/ecovision_mobilenetv2.keras"
    )


if __name__ == "__main__":
    main()
