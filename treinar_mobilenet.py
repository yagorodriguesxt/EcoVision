
from pathlib import Path
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

DATASET = Path("dataset")
IMG_SIZE = (160, 160)
BATCH_SIZE = 16
SEED = 42
EPOCHS_INICIAIS = 5
EPOCHS_AJUSTE = 5


def carregar_dados(pasta, treino=False):
    return keras.utils.image_dataset_from_directory(
        pasta,
        image_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        seed=SEED,
        shuffle=treino,
    )


def main():
    treino_dir = DATASET / "train"
    val_dir = DATASET / "validation"

    if not treino_dir.is_dir() or not val_dir.is_dir():
        raise FileNotFoundError(
            "Prepare dataset/train e dataset/validation antes de treinar."
        )

    treino = carregar_dados(treino_dir, treino=True)
    validacao = carregar_dados(val_dir)

    classes = treino.class_names
    if len(classes) != 3:
        raise ValueError(f"Esperadas 3 classes, encontradas: {classes}")

    print("Classes:", classes)

    aumento = keras.Sequential([
        layers.RandomFlip("horizontal"),
        layers.RandomRotation(0.08),
        layers.RandomZoom(0.1),
    ])

    base = keras.applications.MobileNetV2(
        input_shape=(*IMG_SIZE, 3),
        include_top=False,
        weights="imagenet",
    )
    base.trainable = False

    entrada = keras.Input(shape=(*IMG_SIZE, 3))
    x = aumento(entrada)
    x = layers.Rescaling(1.0)(x)
    x = keras.applications.mobilenet_v2.preprocess_input(x)
    x = base(x, training=False)
    x = layers.GlobalAveragePooling2D()(x)
    x = layers.Dropout(0.2)(x)
    saida = layers.Dense(len(classes), activation="softmax")(x)

    modelo = keras.Model(entrada, saida)
    modelo.compile(
        optimizer=keras.optimizers.Adam(learning_rate=1e-3),
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"],
    )

    modelo.fit(
        treino,
        validation_data=validacao,
        epochs=EPOCHS_INICIAIS,
    )

    # Ajuste fino de parte das camadas finais.
    base.trainable = True
    for camada in base.layers[:-30]:
        camada.trainable = False

    modelo.compile(
        optimizer=keras.optimizers.Adam(learning_rate=1e-5),
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"],
    )

    modelo.fit(
        treino,
        validation_data=validacao,
        epochs=EPOCHS_AJUSTE,
    )

    Path("modelos").mkdir(exist_ok=True)
    modelo.save("modelos/ecovision_mobilenet.keras")
    print("Modelo salvo em modelos/ecovision_mobilenet.keras")


if __name__ == "__main__":
    main()
