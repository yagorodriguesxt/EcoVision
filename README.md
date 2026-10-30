# EcoVision: classificação de resíduos recicláveis

O EcoVision é um projeto acadêmico que utiliza visão computacional e aprendizado profundo para classificar imagens de resíduos em três categorias: **metal, papel e plástico**.

O projeto possui duas partes: treinamento e avaliação dos modelos neste repositório e aplicativo Android para realizar a classificação localmente.

**Aplicativo Android:** https://github.com/yagorodriguesxt/EcoVision-Android

## Objetivo

Apoiar a identificação de materiais recicláveis por meio de imagens, contribuindo para a separação adequada dos resíduos.

## Conjunto de dados utilizado

O conjunto preparado para o experimento contém **300 imagens**, distribuídas igualmente entre as três classes:

| Classe | Total de imagens | Fotos próprias |
|---|---:|---:|
| Metal | 100 | 28 |
| Papel | 100 | 30 |
| Plástico | 100 | 30 |
| **Total** | **300** | **88** |

As imagens próprias foram incluídas no subconjunto de treinamento. O conjunto também utiliza imagens obtidas de uma base pública de resíduos (TrashNet).

### Divisão

| Subconjunto | Imagens | Percentual |
|---|---:|---:|
| Treinamento | 210 | 70% |
| Validação | 45 | 15% |
| Teste | 45 | 15% |
| **Total** | **300** | **100%** |

As imagens estão organizadas por subconjunto e classe na estrutura de pastas utilizada pelo TensorFlow. **Os arquivos de imagem do conjunto preparado não estão incluídos neste repositório neste momento**; a demonstração do conjunto e de sua organização é apresentada no vídeo da entrega.

## Modelos

Foram trabalhadas duas abordagens:

- **CNN própria:** modelo de referência (*baseline*).
- **MobileNetV2:** arquitetura pré-treinada, utilizada com transferência de aprendizado (*transfer learning*) e ajuste fino (*fine-tuning*).

O treinamento da MobileNetV2 utiliza imagens de 160 × 160 pixels, aumento de dados e pré-processamento incorporado ao modelo.

## Resultado registrado

Na avaliação registrada para a MobileNetV2, foram obtidos:

- **Acurácia no conjunto de teste: 84,44% (38 acertos em 45 imagens).**
- Papel: 15 de 15 imagens classificadas corretamente.
- Metal: 12 de 15 imagens classificadas corretamente.
- Plástico: 11 de 15 imagens classificadas corretamente.

O conjunto de teste possui 45 imagens, portanto os resultados representam este experimento e não garantem o mesmo desempenho em todas as condições reais de uso.

## Aplicativo Android

O aplicativo utiliza um modelo TensorFlow Lite para realizar a inferência no próprio dispositivo. A proposta inclui captura de imagem pela câmera e seleção de imagem pela galeria.

Repositório: https://github.com/yagorodriguesxt/EcoVision-Android

## Estrutura do repositório

- `treinar_modelo.py`: treinamento da CNN de referência.
- `treinar_mobilenet.py`: treinamento e ajuste fino da MobileNetV2.
- `avaliar_modelos.py`: cálculo de métricas e matriz de confusão.
- `converter_tflite.py`: conversão do modelo Keras para TensorFlow Lite.
- `requirements.txt`: dependências Python.
- `dataset/`: documentação e estrutura de pastas do conjunto de dados.

## Como preparar o ambiente

Instale as dependências:

```bash
pip install -r requirements.txt
```

Organize o conjunto de dados nas pastas `dataset/train`, `dataset/validation` e `dataset/test`, cada uma contendo as subpastas `metal`, `papel` e `plastico`.

Para treinar a MobileNetV2:

```bash
python treinar_mobilenet.py
```

Para avaliar os modelos disponíveis:

```bash
python avaliar_modelos.py
```

Para converter o modelo treinado:

```bash
python converter_tflite.py
```

## Limitações e cuidados

- O conjunto de teste é pequeno e não representa todas as variações de resíduos, iluminação, fundo e ângulo.
- A classificação indica semelhança visual com as classes treinadas; não substitui as regras locais de coleta seletiva.
- Acurácia experimental não é garantia de desempenho universal.
- A origem e as condições de uso das imagens devem ser respeitadas.

## Etapa 1

A primeira entrega apresenta o tema de descarte de resíduos recicláveis, o conjunto de dados adotado, o aplicativo e suas telas de câmera e galeria por meio de vídeo demonstrativo de até três minutos.
