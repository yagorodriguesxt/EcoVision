# Conjunto de Dados | EcoVision

## Classes e quantidades

O conjunto preparado para o experimento contém 300 imagens, distribuídas igualmente:

| Classe | Total | Fotos próprias |
|---|---:|---:|
| `papel` | 100 | 30 |
| `plastico` | 100 | 30 |
| `metal` | 100 | 28 |
| **Total** | **300** | **88** |

As imagens próprias foram incluídas no subconjunto de treinamento. O conjunto também utiliza imagens provenientes da base pública TrashNet.

## Divisão utilizada

| Subconjunto | Imagens | Percentual |
|---|---:|---:|
| Treinamento | 210 | 70% |
| Validação | 45 | 15% |
| Teste | 45 | 15% |
| **Total** | **300** | **100%** |

## Estrutura

```text
dataset/
├── train/
│   ├── metal/
│   ├── papel/
│   └── plastico/
├── validation/
│   ├── metal/
│   ├── papel/
│   └── plastico/
└── test/
    ├── metal/
    ├── papel/
    └── plastico/
```

**Observação:** este repositório contém a documentação e as pastas de referência, mas os arquivos de imagem do conjunto preparado não estão versionados nele. O conjunto completo foi utilizado localmente no treinamento e é apresentado na demonstração da entrega.
