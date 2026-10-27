
from pathlib import Path
import json

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)

DATASET = Path("dataset/test")
MODELOS = {
    "cnn": Path("modelos/ecovision_cnn.keras"),
    "mobilenet": Path("modelos/ecovision_mobilenet.keras"),
}
IMG_SIZE = (160, 160)
BATCH_SIZE = 16


def main():
    if not DATASET.is_dir():
        raise FileNotFoundError(
            "A pasta dataset/test ainda não foi preparada."
        )

    dados = tf.keras.utils.image_dataset_from_directory(
        DATASET,
        image_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        shuffle=False,
    )

    classes = dados.class_names
    y_real = np.concatenate([y.numpy() for _, y in dados], axis=0)

    Path("resultados").mkdir(exist_ok=True)

    for nome, caminho in MODELOS.items():
        if not caminho.is_file():
            print(f"Modelo ainda não encontrado: {caminho}")
            continue

        modelo = tf.keras.models.load_model(caminho)
        probabilidades = modelo.predict(dados, verbose=0)
        y_previsto = np.argmax(probabilidades, axis=1)

        acuracia = accuracy_score(y_real, y_previsto)
        matriz = confusion_matrix(
            y_real,
            y_previsto,
            labels=range(len(classes)),
        )
        relatorio = classification_report(
            y_real,
            y_previsto,
            labels=range(len(classes)),
            target_names=classes,
            output_dict=True,
            zero_division=0,
        )

        resultado = {
            "modelo": nome,
            "classes": classes,
            "acuracia": float(acuracia),
            "relatorio_por_classe": relatorio,
            "matriz_confusao": matriz.tolist(),
        }

        arquivo_json = Path("resultados") / f"{nome}_metricas.json"
        arquivo_json.write_text(
            json.dumps(resultado, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )

        fig, ax = plt.subplots(figsize=(6, 5))
        imagem = ax.imshow(matriz)
        ax.set(
            xticks=range(len(classes)),
            yticks=range(len(classes)),
            xticklabels=classes,
            yticklabels=classes,
            xlabel="Classe prevista",
            ylabel="Classe real",
            title=f"Matriz de confusão: {nome}",
        )
        plt.setp(ax.get_xticklabels(), rotation=30, ha="right")

        for i in range(len(classes)):
            for j in range(len(classes)):
                ax.text(j, i, str(matriz[i, j]), ha="center", va="center")

        fig.colorbar(imagem, ax=ax)
        fig.tight_layout()
        fig.savefig(
            Path("resultados") / f"{nome}_matriz_confusao.png",
            dpi=150,
        )
        plt.close(fig)

        print(f"\nModelo: {nome}")
        print(f"Acurácia: {acuracia:.4f}")
        print(classification_report(
            y_real,
            y_previsto,
            labels=range(len(classes)),
            target_names=classes,
            zero_division=0,
        ))
        print(f"Métricas salvas em {arquivo_json}")


if __name__ == "__main__":
    main()
