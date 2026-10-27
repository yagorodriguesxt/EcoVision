# EcoVision ♻️

**Classificação de resíduos recicláveis por visão computacional**

## 1. Sobre o projeto

O EcoVision é um projeto acadêmico que propõe utilizar inteligência artificial para classificar resíduos recicláveis a partir de imagens, auxiliando na identificação e na separação de materiais para reciclagem.

O sistema terá como classes de classificação:

- **Papel**
- **Plástico**
- **Metal**

A proposta é desenvolver um aplicativo móvel capaz de realizar a classificação localmente, sem depender de conexão com a internet durante a inferência do modelo.

## 2. Objetivo

Desenvolver e avaliar um modelo de classificação de imagens e integrá-lo a um aplicativo móvel, explorando técnicas de aprendizado profundo e visão computacional.

## 3. Metodologia planejada

O desenvolvimento seguirá estas etapas:

1. Coleta e organização das imagens do conjunto de dados.
2. Separação dos dados em treinamento, validação e teste.
3. Desenvolvimento de uma rede neural convolucional (CNN) própria como modelo de referência.
4. Aplicação de transferência de aprendizado com uma arquitetura compatível, como MobileNetV2.
5. Aplicação de aumento de dados (*data augmentation*) e ajuste fino (*fine-tuning*).
6. Avaliação dos modelos com métricas de classificação e matriz de confusão.
7. Conversão do modelo selecionado para o formato TensorFlow Lite.
8. Desenvolvimento e teste do aplicativo móvel com funcionamento offline.

## 4. Requisitos do conjunto de dados

O conjunto de dados deverá conter, no mínimo, 100 imagens por classe, respeitando a exigência de que pelo menos 25% das imagens de cada classe sejam fotografadas pelo autor do projeto.

A divisão planejada será:

- 70% para treinamento;
- 15% para validação;
- 15% para teste.

A origem das imagens e os critérios de divisão serão documentados durante o desenvolvimento.

## 5. Funcionalidades previstas

- Classificação de resíduos por imagem.
- Captura de imagens pela câmera.
- Seleção de imagens da galeria.
- Histórico de classificações.
- Inferência local, sem necessidade de internet para classificar imagens.

## 6. Tecnologias previstas

- Python
- TensorFlow e Keras
- MobileNetV2
- TensorFlow Lite
- Ferramentas de desenvolvimento para aplicativos móveis
- Git e GitHub

As tecnologias e suas versões poderão ser ajustadas conforme os testes de compatibilidade.

## 7. Status do desenvolvimento

**Etapa atual:** organização inicial do projeto e preparação do ambiente de desenvolvimento.

As funcionalidades, o treinamento do modelo e as métricas serão registrados à medida que forem implementados e testados.

## 8. Uso de inteligência artificial generativa

Ferramentas de inteligência artificial generativa poderão ser utilizadas como apoio ao planejamento, à documentação, à compreensão de conceitos e à elaboração de código. O uso será informado de acordo com as atividades efetivamente realizadas, e os resultados serão revisados e testados durante o desenvolvimento.

---

Projeto acadêmico desenvolvido para estudo de aprendizado profundo, classificação de imagens e aplicações móveis de visão computacional.
# EcoVision
