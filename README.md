# EcoVision ♻️

Aplicativo móvel para classificação de resíduos recicláveis por meio de inteligência artificial, utilizando visão computacional e um modelo de classificação executado localmente no dispositivo.

O EcoVision tem como objetivo auxiliar na identificação de resíduos e incentivar o descarte adequado, contribuindo para práticas mais sustentáveis.

## 1. Classes de classificação

O aplicativo foi desenvolvido para classificar resíduos em três categorias:

- **Papel**
- **Plástico**
- **Metal**

## 2. Objetivo

Desenvolver, treinar e avaliar modelos de classificação de imagens e integrá-los a um aplicativo móvel Android capaz de realizar inferências localmente, sem depender de conexão com a internet durante a classificação.

O projeto também compara uma rede neural convolucional desenvolvida como referência com uma arquitetura baseada em transferência de aprendizado.

## 3. Metodologia

O desenvolvimento do EcoVision contempla as seguintes etapas:

1. Obtenção e organização das imagens.
2. Verificação da integridade do conjunto de dados.
3. Divisão dos dados em treinamento, validação e teste.
4. Desenvolvimento de uma CNN de referência.
5. Treinamento com transferência de aprendizado utilizando MobileNetV2.
6. Aplicação de aumento de dados (*data augmentation*) e ajuste fino (*fine-tuning*).
7. Avaliação dos modelos por meio de métricas de classificação e matriz de confusão.
8. Conversão do modelo selecionado para TensorFlow Lite.
9. Integração do modelo ao aplicativo Android.
10. Testes de classificação, navegação e histórico.

## 4. Conjunto de dados

O conjunto inicial utiliza imagens públicas de resíduos recicláveis, organizadas nas classes papel, plástico e metal.

A divisão inicial foi realizada com a seguinte proporção:

- **70%** para treinamento.
- **15%** para validação.
- **15%** para teste.

### Quantidade de imagens na divisão inicial

| Classe | Treinamento | Validação | Teste | Total |
|---|---:|---:|---:|---:|
| Metal | 287 | 61 | 62 | 410 |
| Papel | 415 | 89 | 90 | 594 |
| Plástico | 337 | 72 | 73 | 482 |
| **Total** | **1.039** | **222** | **225** | **1.486** |

**Observação:** essa divisão corresponde ao conjunto público utilizado nos experimentos preliminares. Ainda é necessário incorporar fotografias próprias, garantir que pelo menos 25% das imagens de cada classe sejam de autoria do desenvolvedor e realizar a avaliação final com a divisão atualizada.

## 5. Modelos desenvolvidos

### CNN de referência

Foi implementada uma rede neural convolucional treinada a partir do conjunto de dados, servindo como referência para a comparação com modelos de transferência de aprendizado.

### MobileNetV2

Foi utilizada a arquitetura MobileNetV2 com pesos pré-treinados no ImageNet. O treinamento incluiu aumento de dados e ajuste fino de parte das camadas da rede.

A arquitetura foi selecionada considerando o objetivo de executar a classificação em um dispositivo móvel.

## 6. Resultados preliminares

Os primeiros experimentos produziram os seguintes resultados no conjunto de teste inicial:

| Modelo | Acurácia |
|---|---:|
| CNN de referência | 67,56% |
| MobileNetV2 | 94,67% |
| MobileNetV2 convertido para TensorFlow Lite | 94,67% |

A MobileNetV2 apresentou desempenho superior ao da CNN de referência nesses experimentos, com uma diferença de 27,11 pontos percentuais na acurácia.

A versão convertida para TensorFlow Lite manteve a mesma acurácia observada na avaliação realizada no ambiente de treinamento.

**Importante:** os valores apresentados são preliminares e foram obtidos com o conjunto público inicial. Eles deverão ser reavaliados após a inclusão das fotografias próprias exigidas pelo projeto. Os resultados não representam, por si só, uma validação definitiva do desempenho em condições reais de uso.

## 7. Aplicativo móvel

O aplicativo EcoVision está sendo desenvolvido para Android, com interface em português brasileiro e foco na facilidade de utilização.

As funcionalidades implementadas ou em desenvolvimento incluem:

- Classificação de resíduos por imagem.
- Captura de imagens pela câmera.
- Seleção de imagens da galeria.
- Exibição da classe prevista e da confiança da classificação.
- Orientações gerais sobre descarte.
- Histórico de classificações.
- Execução local do modelo TensorFlow Lite.

O aplicativo utiliza o arquivo `ecovision_mobilenetv2.tflite` para realizar as classificações no dispositivo, sem enviar as imagens para um serviço de inteligência artificial na nuvem.

Os testes realizados no ambiente de desenvolvimento incluíram imagens de exemplo das três classes e a verificação da exibição e do armazenamento do histórico. A compatibilidade com diferentes dispositivos e o funcionamento completo da câmera e da galeria ainda precisam ser verificados em condições reais.

## 8. Tecnologias utilizadas

- Python
- TensorFlow e Keras
- MobileNetV2
- TensorFlow Lite
- Google Colab
- Google Drive
- Kotlin e Jetpack Compose
- Git e GitHub

## 9. Estrutura do repositório

- `dataset/`: estrutura destinada à organização dos dados de treinamento, validação e teste.
- `treinar_modelo.py`: treinamento da CNN de referência.
- `treinar_mobilenet.py`: treinamento da MobileNetV2.
- `avaliar_modelos.py`: avaliação dos modelos e geração de métricas.
- `converter_tflite.py`: conversão do modelo para TensorFlow Lite.
- `PLANEJAMENTO.md`: planejamento técnico do projeto.
- `ENTREGA-1.md`: documentação da primeira entrega.
- `requirements.txt`: dependências Python do projeto.

Os modelos treinados e os arquivos de resultados são mantidos no ambiente de desenvolvimento enquanto a organização da entrega final é preparada.

## 10. Status do desenvolvimento

**Concluído nos experimentos preliminares:**

- Organização inicial do conjunto público de imagens.
- Divisão dos dados em treinamento, validação e teste.
- Treinamento da CNN de referência.
- Treinamento e ajuste fino da MobileNetV2.
- Avaliação dos dois modelos.
- Conversão do modelo selecionado para TensorFlow Lite.
- Testes preliminares de classificação no aplicativo Android.

**Pendente para a entrega final:**

- Incorporar as fotografias próprias e cumprir a proporção mínima exigida por classe.
- Repetir o treinamento e a avaliação com o conjunto definitivo.
- Documentar a análise dos erros e os resultados finais.
- Validar o funcionamento offline e testar câmera e galeria em um dispositivo compatível.
- Finalizar a documentação e gravar o vídeo de demonstração.

## 11. Uso de inteligência artificial generativa

Ferramentas de inteligência artificial generativa foram utilizadas como apoio ao planejamento, à documentação, à organização do desenvolvimento, à elaboração e revisão de código e à resolução de dúvidas técnicas.

O projeto tem finalidade acadêmica e busca demonstrar a aplicação prática de técnicas de aprendizado profundo, classificação de imagens e integração de modelos de inteligência artificial em aplicações móveis.

## 12. Considerações finais

O EcoVision explora a utilização de visão computacional para auxiliar na identificação de resíduos recicláveis. Os experimentos preliminares indicam que a MobileNetV2 é uma alternativa promissora para a classificação das três categorias propostas.

A conclusão do projeto depende da inclusão das fotografias próprias, da avaliação final do modelo e da validação do aplicativo em condições reais de utilização.
