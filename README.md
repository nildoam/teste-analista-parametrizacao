# Teste Técnico — Analista de Dados / Parametrização

Este repositório apresenta a solução desenvolvida para o teste técnico de **Analista de Dados/Parametrização**, com foco na interpretação de requisitos, estruturação de regras de negócio e tradução dessas regras para uma lógica de parametrização rastreável e testável.

A proposta foi organizada para demonstrar o caminho entre a análise funcional e a implementação:

**Requisito → Regra de negócio → Matriz de decisão → Fluxograma → Pseudocódigo → Implementação → Teste**

---

## Objetivo

O objetivo da solução é estruturar os critérios lógicos necessários para determinar a aplicabilidade das rubricas relacionadas a:

- **IRRF** — Imposto de Renda Retido na Fonte;
- **RGPS/INSS** — contribuição ao Regime Geral de Previdência Social;
- **RPPS** — contribuição ao Regime Próprio de Previdência Social.

Com base no agrupamento das regras apresentadas no teste, foram propostas **3 rubricas de desconto**, compartilhadas pelos vínculos que possuem a mesma natureza de incidência.

A solução concentra-se na decisão sobre **quando uma rubrica deve ou não ser aplicada**, independentemente da fórmula utilizada posteriormente para cálculo de seu valor.

---

## Estrutura da solução

A entrega foi dividida em três componentes principais:

### 1. Documentação funcional e técnica

Contém a análise dos requisitos, dados de entrada, regras de negócio, matrizes de decisão, exceções, pseudocódigo e cenários de teste.

➡️ [Acessar documentação técnica](docs/solucao-parametrizacao.md)

### 2. Fluxos de decisão

Representam graficamente as principais decisões relacionadas ao enquadramento previdenciário e ao IRRF.

➡️ [Visualizar fluxogramas](docs/diagramas/README.md)

Arquivos-fonte:

- [Fluxo previdenciário](docs/diagramas/fluxo-previdenciario.mmd)
- [Fluxo de IRRF](docs/diagramas/fluxo-irrf.mmd)

### 3. Implementação de referência

Demonstra em Python como as regras documentadas podem ser traduzidas para uma lógica computacional simples e testável.

➡️ [Consultar implementação](src/regras_parametrizacao.py)

➡️ [Consultar cenários de teste](src/test_regras_parametrizacao.py)

➡️ [Documentação da implementação](src/README.md)

---

## Visão geral do processamento

A solução utiliza inicialmente os dados cadastrais e funcionais do servidor para determinar seu enquadramento.

O processamento pode ser resumido da seguinte forma:

```text
Servidor / Vínculo
        │
        ▼
 Validação da vigência
        │
        ▼
Identificação do regime
        │
        ├──────────────┐
        ▼              ▼
 Previdência         IRRF
        │              │
        ▼              ▼
 RGPS / RPPS       Tributação
 / Específico      / Isenção
        │              │
        └──────┬───────┘
               ▼
      Rubricas aplicáveis
               +
       Ocorrências para
            análise
```

As decisões previdenciárias e tributárias são avaliadas de forma independente, permitindo combinações como:

- `RGPS + IRRF`;
- `RPPS + IRRF`;
- somente `RGPS`;
- somente `RPPS`;
- nenhuma rubrica;
- ocorrência para análise.

---

## Princípios adotados

A solução foi construída considerando alguns princípios de parametrização:

**Rastreabilidade**  
Cada resultado deve poder ser relacionado à regra que o produziu.

**Separação de responsabilidades**  
As regras previdenciárias e tributárias são avaliadas separadamente.

**Vigência**  
Vínculos, isenções e demais condições são avaliados considerando a competência processada.

**Falha segura**  
Uma condição desconhecida ou inconsistente não deve gerar automaticamente uma rubrica de desconto.

**Parametrização**  
Informações sujeitas a alteração devem, sempre que possível, ser tratadas como parâmetros e não como valores fixos na implementação.

---

## Cenários de validação

A implementação inclui testes para diferentes situações, entre elas:

| Cenário | Resultado esperado |
|---|---|
| Efetivo RPPS, tributável e sem isenção | `RPPS + IRRF` |
| Temporário, tributável e sem isenção | `RGPS + IRRF` |
| RGPS com isenção de IRRF vigente | `RGPS` |
| Inativo/Aposentado com isenção vigente | Sem `IRRF` |
| Vínculo encerrado | Nenhuma rubrica |
| Regime não identificado | Ocorrência para análise |
| Regime militar | Tratamento previdenciário específico |

Os cenários completos estão descritos na [documentação técnica](docs/solucao-parametrizacao.md#12-cenários-de-teste).

---

## Executando a implementação

A implementação utiliza apenas recursos da biblioteca padrão do Python.

Para executar o exemplo:

```bash
python src/regras_parametrizacao.py
```

Resultado esperado:

```text
{
    'rubricas': ['RPPS', 'IRRF'],
    'ocorrencias': []
}
```

### Executando os testes

A partir da raiz do repositório:

```bash
python -m unittest src/test_regras_parametrizacao.py
```

Quando as regras e a implementação estiverem consistentes, os testes deverão ser concluídos sem falhas.

---

## Como avaliar esta solução

Uma sequência sugerida para análise da entrega é:

1. consultar a [documentação técnica](docs/solucao-parametrizacao.md);
2. visualizar os [fluxos de decisão](docs/diagramas/README.md);
3. consultar a [implementação de referência](src/regras_parametrizacao.py);
4. verificar os [cenários de teste](src/test_regras_parametrizacao.py).

Essa sequência permite acompanhar a transformação dos requisitos funcionais em regras, decisões e implementação.

---

## Estrutura do repositório

```text
teste-analista-parametrizacao/
│
├── README.md
│
├── docs/
│   ├── README.md
│   ├── solucao-parametrizacao.md
│   └── diagramas/
│       ├── README.md
│       ├── fluxo-previdenciario.mmd
│       └── fluxo-irrf.mmd
│
└── src/
    ├── README.md
    ├── regras_parametrizacao.py
    └── test_regras_parametrizacao.py
```

---

## Escopo

A implementação possui caráter de **prova de conceito** e tem como objetivo demonstrar a interpretação e estruturação das regras apresentadas no teste.

Não fazem parte do escopo o cálculo financeiro das rubricas, tabelas progressivas, alíquotas, persistência em banco de dados ou integração com sistemas externos.

---

**Francinildo Vieira**  
Teste Técnico — Analista de Dados / Parametrização
