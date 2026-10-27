
from pathlib import Path
import tensorflow as tf

ORIGEM = Path("modelos/ecovision_mobilenet.keras")
DESTINO = Path("modelos/ecovision_mobilenet.tflite")


def main():
    if not ORIGEM.is_file():
        raise FileNotFoundError(
            "Modelo treinado não encontrado. "
            "Execute primeiro treinar_mobilenet.py."
        )

    modelo = tf.keras.models.load_model(ORIGEM)

    conversor = tf.lite.TFLiteConverter.from_keras_model(modelo)
    conversor.optimizations = [tf.lite.Optimize.DEFAULT]

    modelo_tflite = conversor.convert()

    DESTINO.parent.mkdir(parents=True, exist_ok=True)
    DESTINO.write_bytes(modelo_tflite)

    # Verifica se o arquivo pode ser carregado pelo interpretador.
    interpretador = tf.lite.Interpreter(model_path=str(DESTINO))
    interpretador.allocate_tensors()

    print(f"Modelo convertido e validado: {DESTINO}")
    print(f"Tamanho: {DESTINO.stat().st_size / 1024:.1f} KB")


if __name__ == "__main__":
    main()
