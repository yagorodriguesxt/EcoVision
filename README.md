# EcoVision: treinamento e documentação do modelo

Projeto de classificação de imagens de resíduos em três classes: metal, papel e plástico.

Aplicativo Android: https://github.com/yagorodriguesxt/EcoVision-Android

## Objetivo
Treinar e avaliar modelos de classificação de imagens e disponibilizar um modelo TensorFlow Lite para uso local no aplicativo.

## Conjunto reduzido registrado
| Classe | Imagens |
|---|---:|
| Metal | 112 |
| Papel | 120 |
| Plástico | 120 |
| **Total** | **352** |

A divisão registrada foi de 246 imagens para treino, 53 para validação e 53 para teste. Também foi anotada a inclusão de pelo menos 25% de imagens próprias por classe no treinamento. Confira os scripts e os arquivos finais para confirmar que esses números correspondem à versão entregue.

## Métricas registradas no conjunto de teste reduzido
| Classe | Precisão | Recall | F1 |
|---|---:|---:|---:|
| Metal | 93,75% | 88,24% | 90,91% |
| Papel | 90,00% | 100,00% | 94,74% |
| Plástico | 94,12% | 88,89% | 91,43% |

Foram anotadas acurácias de 92,45% em Keras e 94,34% em TensorFlow Lite, sobre um conjunto de teste de 53 imagens. Antes de apresentar a diferença como comparação conclusiva, reproduza os resultados e explique a metodologia.

## Cuidados
- Um conjunto de teste pequeno pode não representar imagens reais variadas.
- Evite imagens duplicadas ou quase idênticas em divisões diferentes.
- Registre versões de bibliotecas, sementes aleatórias e divisão de dados para permitir reprodução.
- Não trate as métricas como garantia de desempenho universal.

## Modelo TensorFlow Lite
As anotações técnicas indicam entrada RGB de 160 × 160 pixels, valores [0, 255] e pré-processamento no grafo. Confirme isso no modelo final antes de substituir arquivos.

Ordem de classes anotada:
1. Metal
2. Papel
3. Plástico

Ao alterar o modelo, mantenha os índices alinhados com os rótulos do aplicativo.

## Reprodutibilidade
Registre origem do conjunto de dados, contagens por classe, divisão treino/validação/teste, arquitetura baseline, transfer learning, métricas por classe, matriz de confusão, versão do `.tflite` e versões das bibliotecas.

O teste bem-sucedido do APK em um celular, relatado em 28/10/2026, confirma o funcionamento observado no dispositivo, mas não substitui a avaliação reprodutível do modelo.
