# Entrega 1 | EcoVision

## 1. Identificação

**Projeto:** EcoVision  
**Tema:** Descarte de resíduos recicláveis  
**Objetivo:** classificar imagens de resíduos em três categorias: papel, plástico e metal.  
**Repositório público:** https://github.com/yagorodriguesxt/EcoVision

## 2. Descrição do projeto

O EcoVision é um aplicativo Android que utiliza inteligência artificial e visão computacional para identificar resíduos recicláveis por meio de imagens. O usuário pode capturar uma imagem com a câmera do celular ou selecionar uma imagem armazenada na galeria. O modelo realiza a classificação em uma das três categorias trabalhadas: papel, plástico ou metal.

## 3. Conjunto de dados

O conjunto preparado para o projeto possui 300 imagens, distribuídas igualmente entre as três classes:

| Classe | Imagens | Fotos próprias |
|---|---:|---:|
| Papel | 100 | 30 |
| Plástico | 100 | 30 |
| Metal | 100 | 28 |
| **Total** | **300** | **88** |

A divisão utilizada foi de 70% para treinamento, 15% para validação e 15% para teste.

## 4. Aplicativo

O aplicativo Android utiliza um modelo TensorFlow Lite para realizar a classificação localmente. Na demonstração, devem ser apresentadas as telas e as funcionalidades efetivamente implementadas, incluindo:

- Abertura e apresentação do aplicativo.
- Captura de imagem pela câmera.
- Seleção de imagem pela galeria.
- Exibição do resultado da classificação.

## 5. Vídeo demonstrativo

O vídeo da Etapa 1 deve ter duração máxima de três minutos e apresentar:

1. O tema escolhido: descarte de resíduos.
2. O conjunto de dados adotado e suas três classes.
3. As telas do aplicativo.
4. A demonstração da câmera e da galeria.

## 6. Repositório

O código e a documentação do treinamento estão disponíveis no repositório público:

https://github.com/yagorodriguesxt/EcoVision

