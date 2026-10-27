# Planejamento Técnico | EcoVision

## 1. Identificação do projeto

**Nome:** EcoVision  
**Área:** Inteligência Artificial e Visão Computacional  
**Aplicação:** Classificação de resíduos recicláveis por imagens.

## 2. Problema e proposta

A identificação correta dos materiais recicláveis pode auxiliar na separação dos resíduos. O EcoVision propõe utilizar um modelo de aprendizado profundo para classificar imagens em três categorias: papel, plástico e metal.

O modelo deverá ser integrado a um aplicativo móvel com processamento local, permitindo realizar classificações sem depender de conexão com a internet durante a inferência.

## 3. Classes de classificação

| Classe | Descrição |
|---|---|
| Papel | Resíduos constituídos predominantemente de papel |
| Plástico | Objetos e embalagens de plástico |
| Metal | Objetos e embalagens de metal |

## 4. Conjunto de dados

O conjunto de dados deverá atender aos seguintes requisitos:

- Pelo menos 100 imagens por classe.
- No mínimo 25% das imagens de cada classe fotografadas pelo autor.
- Organização das imagens por classe.
- Separação entre treinamento, validação e teste.
- Registro da origem das imagens e dos critérios utilizados na organização.

### Divisão planejada

| Subconjunto | Percentual |
|---|---:|
| Treinamento | 70% |
| Validação | 15% |
| Teste | 15% |

A divisão será realizada evitando que imagens duplicadas ou praticamente idênticas apareçam em subconjuntos diferentes.

## 5. Desenvolvimento dos modelos

### 5.1 Modelo de referência

Será desenvolvida uma rede neural convolucional (CNN) própria para estabelecer uma referência inicial de desempenho.

### 5.2 Transferência de aprendizado

Será utilizada uma arquitetura pré-treinada compatível com dispositivos móveis, inicialmente a MobileNetV2.

Serão avaliadas técnicas de aumento de dados (*data augmentation*) e ajuste fino (*fine-tuning*), conforme os resultados obtidos.

## 6. Avaliação

A avaliação deverá incluir:

- Acurácia.
- Precisão.
- Revocação (*recall*).
- F1-score.
- Matriz de confusão.
- Análise de erros e exemplos de classificações incorretas.

Os resultados serão calculados com dados de teste que não tenham sido utilizados no treinamento ou na seleção dos hiperparâmetros.

## 7. Integração com o aplicativo

O modelo selecionado será convertido para TensorFlow Lite (`.tflite`) e integrado ao aplicativo móvel.

### Funcionalidades previstas

1. Tela inicial.
2. Captura de imagens pela câmera.
3. Seleção de imagens da galeria.
4. Exibição da classe prevista.
5. Histórico de classificações.
6. Funcionamento offline para inferência.

## 8. Critérios de conclusão

O projeto será considerado concluído após a implementação e verificação das seguintes etapas:

- Conjunto de dados documentado conforme os requisitos.
- CNN própria treinada e avaliada.
- Modelo com transferência de aprendizado treinado e avaliado.
- Comparação dos modelos e análise dos erros.
- Modelo exportado para `.tflite`.
- Aplicativo integrado e testado.
- Repositório público com código e instruções de execução.
- Vídeo demonstrativo das funcionalidades exigidas.

## 9. Organização e transparência

O desenvolvimento será registrado no GitHub por meio de commits que representem etapas reais do trabalho.

Ferramentas de inteligência artificial generativa poderão ser utilizadas como apoio à documentação, ao planejamento e à programação. Seu uso será descrito de acordo com as atividades efetivamente realizadas.

## 10. Status atual

**Fase:** planejamento inicial.

As etapas técnicas, os resultados experimentais e as funcionalidades implementadas serão atualizados durante o desenvolvimento. Nenhum resultado de treinamento ou teste será declarado antes de sua execução e verificação.
