
from pathlib import Path
import tensorflow as tf

ORIGEM = Path("modelos/ecovision_mobilenetv2.keras")
DESTINO = Path("modelos/ecovision_mobilenetv2.tflite")


def main():
    if not ORIGEM.is_file():
        raise FileNotFoundError(
            f"Modelo não encontrado: {ORIGEM}. "
            "Execute treinar_mobilenet.py primeiro."
        )

    modelo = tf.keras.models.load_model(ORIGEM)

    conversor = tf.lite.TFLiteConverter.from_keras_model(modelo)
    conversor.optimizations = [tf.lite.Optimize.DEFAULT]
    modelo_tflite = conversor.convert()

    DESTINO.parent.mkdir(parents=True, exist_ok=True)
    DESTINO.write_bytes(modelo_tflite)

    # Verifica se o arquivo convertido pode ser carregado.
    interpretador = tf.lite.Interpreter(
        model_path=str(DESTINO)
    )
    interpretador.allocate_tensors()

    entrada = interpretador.get_input_details()[0]
    saida = interpretador.get_output_details()[0]

    print(f"Modelo convertido: {DESTINO}")
    print(f"Tamanho: {DESTINO.stat().st_size / 1024:.1f} KB")
    print(f"Formato da entrada: {entrada['shape']}")
    print(f"Tipo da entrada: {entrada['dtype']}")
    print(f"Formato da saída: {saida['shape']}")


if __name__ == "__main__":
    main()
