
from pathlib import Path
import json

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

DATASET = Path("dataset")
IMG_SIZE = (160, 160)
BATCH_SIZE = 16
SEED = 42
EPOCHS = 10

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


def criar_cnn(numero_classes):
    modelo = keras.Sequential([
        layers.Input(shape=(*IMG_SIZE, 3)),
        layers.Rescaling(1.0 / 255),
        layers.Conv2D(16, 3, activation="relu"),
        layers.MaxPooling2D(),
        layers.Conv2D(32, 3, activation="relu"),
        layers.MaxPooling2D(),
        layers.Conv2D(64, 3, activation="relu"),
        layers.GlobalAveragePooling2D(),
        layers.Dense(64, activation="relu"),
        layers.Dropout(0.3),
        layers.Dense(numero_classes, activation="softmax"),
    ])

    modelo.compile(
        optimizer="adam",
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"],
    )
    return modelo


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

    modelo = criar_cnn(len(classes))
    modelo.summary()

    callbacks = [
        keras.callbacks.EarlyStopping(
            monitor="val_loss",
            patience=3,
            restore_best_weights=True,
        )
    ]

    historico = modelo.fit(
        treino,
        validation_data=validacao,
        epochs=EPOCHS,
        callbacks=callbacks,
    )

    MODELO_DIR.mkdir(parents=True, exist_ok=True)
    RESULTADOS_DIR.mkdir(parents=True, exist_ok=True)

    modelo.save(MODELO_DIR / "ecovision_cnn.keras")

    (RESULTADOS_DIR / "classes.json").write_text(
        json.dumps(classes, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    (RESULTADOS_DIR / "historico_cnn.json").write_text(
        json.dumps(historico.history, indent=2),
        encoding="utf-8",
    )

    print("Modelo salvo em modelos/ecovision_cnn.keras")


if __name__ == "__main__":
    main()
