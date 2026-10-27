
from pathlib import Path
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Diretório com as imagens organizadas por classe.
DATASET = Path("dataset")
IMG_SIZE = (160, 160)
BATCH_SIZE = 16
SEED = 42

TRAIN_DIR = DATASET / "train"
VAL_DIR = DATASET / "validation"

def carregar_dados(diretorio):
    return keras.utils.image_dataset_from_directory(
        diretorio,
        image_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        seed=SEED,
        shuffle=True,
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
            "Prepare dataset/train e dataset/validation "
            "com uma pasta para cada classe antes do treinamento."
        )

    treino = carregar_dados(TRAIN_DIR)
    validacao = carregar_dados(VAL_DIR)

    classes = treino.class_names
    if len(classes) != 3:
        raise ValueError(
            f"Esperadas 3 classes, encontradas: {classes}"
        )

    print("Classes:", classes)

    modelo = criar_cnn(len(classes))
    modelo.summary()

    modelo.fit(
        treino,
        validation_data=validacao,
        epochs=10,
    )

    Path("modelos").mkdir(exist_ok=True)
    modelo.save("modelos/ecovision_cnn.keras")
    print("Modelo salvo em modelos/ecovision_cnn.keras")

if __name__ == "__main__":
    main()
