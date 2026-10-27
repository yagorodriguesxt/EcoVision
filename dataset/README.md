# Conjunto de Dados | EcoVision

## Classes

O conjunto de dados será organizado em três classes:

- `papel`
- `plastico`
- `metal`

## Requisitos

- Mínimo de 100 imagens por classe.
- Pelo menos 25% das imagens de cada classe serão fotografadas pelo autor.
- As imagens deverão representar os materiais de forma variada.
- Imagens duplicadas ou praticamente idênticas deverão ser evitadas.
- A origem das imagens deverá ser registrada.

## Divisão dos dados

A divisão planejada é:

| Subconjunto | Percentual |
|---|---:|
| Treinamento | 70% |
| Validação | 15% |
| Teste | 15% |

A separação deverá ser documentada e realizada antes do treinamento, evitando vazamento de dados entre os subconjuntos.

## Estrutura planejada

```text
dataset/
├── README.md
├── train/
│   ├── papel/
│   ├── plastico/
│   └── metal/
├── validation/
│   ├── papel/
│   ├── plastico/
│   └── metal/
└── test/
    ├── papel/
    ├── plastico/
    └── metal/
```

**Status:** estrutura planejada. As imagens serão adicionadas durante a coleta e organização do conjunto de dados.
