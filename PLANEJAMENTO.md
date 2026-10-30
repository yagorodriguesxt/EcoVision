# Planejamento Técnico | EcoVision

## 1. Identificação

**Nome:** EcoVision  
**Área:** Inteligência Artificial e Visão Computacional  
**Aplicação:** classificação de resíduos recicláveis por imagens.

## 2. Problema e proposta

A identificação correta dos materiais recicláveis pode auxiliar na separação dos resíduos. O EcoVision utiliza um modelo de aprendizado profundo para classificar imagens em três categorias: papel, plástico e metal.

O modelo foi integrado a um aplicativo móvel com processamento local, permitindo realizar classificações sem depender de conexão com a internet durante a inferência.

## 3. Classes

| Classe | Descrição |
|---|---|
| Papel | Resíduos constituídos predominantemente de papel |
| Plástico | Objetos e embalagens de plástico |
| Metal | Objetos e embalagens de metal |

## 4. Conjunto de dados preparado

O conjunto utilizado no experimento contém 300 imagens, sendo 100 por classe. Foram incluídas 30 fotos próprias de papel, 30 de plástico e 28 de metal.

A divisão foi realizada da seguinte forma:

| Subconjunto | Quantidade | Percentual |
|---|---:|---:|
| Treinamento | 210 | 70% |
| Validação | 45 | 15% |
| Teste | 45 | 15% |

## 5. Modelos

### 5.1 CNN de referência

Foi desenvolvida uma rede neural convolucional própria para estabelecer uma referência inicial de desempenho.

### 5.2 MobileNetV2

Foi utilizada a arquitetura MobileNetV2 pré-treinada, com transferência de aprendizado, aumento de dados e ajuste fino das camadas finais.

## 6. Avaliação

A avaliação considera acurácia, precisão, revocação (*recall*), F1-score e matriz de confusão.

No experimento registrado com a MobileNetV2, a acurácia no conjunto de teste foi de 84,44%, correspondente a 38 acertos em 45 imagens. Devido ao tamanho reduzido do teste, esse resultado deve ser interpretado como uma medição experimental, não como garantia de desempenho em qualquer situação.

## 7. Integração com o aplicativo

O modelo foi convertido para TensorFlow Lite e integrado ao aplicativo Android.

As funcionalidades demonstradas incluem captura de imagem pela câmera e seleção de imagem pela galeria, com classificação local no dispositivo.

## 8. Organização e transparência

O desenvolvimento é documentado no GitHub. Os resultados apresentados devem corresponder às execuções efetivamente realizadas, e as limitações do conjunto de dados devem ser consideradas na interpretação das métricas.

Ferramentas de inteligência artificial generativa podem ser utilizadas como apoio à documentação, ao planejamento e à programação. Seu uso deve ser descrito de acordo com as atividades efetivamente realizadas.
