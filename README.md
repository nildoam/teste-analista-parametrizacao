# Teste Técnico — Analista de Dados / Parametrização

Este repositório apresenta a solução desenvolvida para o teste técnico de **Analista de Dados/Parametrização**.

O objetivo da proposta é demonstrar a capacidade de interpretar requisitos funcionais, estruturar regras de negócio e traduzi-las em uma solução de parametrização clara, rastreável e passível de implementação.

## 1. Objetivo

A solução foi estruturada com foco na análise e parametrização das regras apresentadas no teste técnico, considerando:

- identificação dos dados necessários ao processamento;
- definição das regras de negócio;
- organização das condições e decisões;
- tratamento de cenários e exceções;
- representação gráfica dos fluxos de decisão;
- implementação simplificada da lógica como prova de conceito.

A abordagem busca separar a **regra de negócio** da **implementação**, facilitando a manutenção, validação e evolução da solução.

## 2. Estrutura do repositório

```text
teste-analista-parametrizacao/
│
├── README.md
│
├── docs/
│   ├── solucao-parametrizacao.pdf
│   │
│   └── diagramas/
│       ├── fluxo-previdenciario.png
│       ├── fluxo-previdenciario.mmd
│       ├── fluxo-irrf.png
│       └── fluxo-irrf.mmd
│
└── src/
    └── regras_parametrizacao.py
```

### `README.md`

Apresenta uma visão geral do problema, da abordagem utilizada e da organização da solução.

### `docs/`

Contém a documentação técnica detalhada da proposta de parametrização.

### `docs/diagramas/`

Contém os fluxogramas utilizados para representar graficamente as principais decisões das regras de negócio.

Os arquivos-fonte dos diagramas também são mantidos no repositório para permitir manutenção e evolução da documentação.

### `src/`

Contém uma implementação simplificada das regras de parametrização, utilizada como prova de conceito da solução proposta.

## 3. Abordagem adotada

A solução foi organizada em etapas:

1. interpretação dos requisitos apresentados;
2. identificação das informações de entrada;
3. levantamento das regras e condições;
4. organização das regras em matrizes de decisão;
5. identificação de exceções e situações específicas;
6. representação dos processos por meio de fluxogramas;
7. tradução das principais regras para pseudocódigo;
8. implementação simplificada da lógica.

Essa abordagem permite que as regras sejam analisadas inicialmente sob a perspectiva funcional e, posteriormente, traduzidas para uma implementação tecnológica.

## 4. Regras de negócio

A parametrização considera os cenários definidos no teste técnico, incluindo regras relacionadas a:

- enquadramento previdenciário;
- identificação do regime aplicável;
- incidências e retenções;
- tratamento das rubricas;
- condições específicas de processamento;
- cálculo e tratamento do IRRF;
- situações excepcionais previstas nas regras apresentadas.

As regras completas, suas condições e respectivos tratamentos estão descritos na documentação técnica disponível no diretório `docs`.

## 5. Fluxos de decisão

Para facilitar a compreensão das regras, foram definidos fluxogramas representando os principais pontos de decisão da parametrização.

Entre os fluxos documentados estão:

- identificação e tratamento do enquadramento previdenciário;
- avaliação das condições relacionadas ao IRRF.

Os diagramas permitem visualizar as decisões antes de sua tradução para código, facilitando a validação funcional da solução.

## 6. Implementação de referência

O diretório `src` apresenta uma implementação simplificada das principais regras descritas na documentação.

O objetivo do código não é representar um sistema de folha de pagamento completo, mas demonstrar como as regras de negócio podem ser transformadas em uma lógica computacional organizada e testável.

## 7. Premissas da solução

Para elaboração da proposta foram consideradas as seguintes premissas:

- as regras apresentadas no teste constituem a principal referência funcional;
- as decisões devem ser rastreáveis até suas respectivas regras de negócio;
- regras e exceções devem estar claramente separadas;
- parâmetros devem ser utilizados sempre que possível em substituição a valores fixos no código;
- a solução deve permitir evolução sem exigir reestruturação completa da lógica;
- a implementação apresentada possui caráter demonstrativo.

## 8. Tecnologias e recursos utilizados

Para documentação e demonstração da solução foram utilizados:

- **Markdown** — documentação do repositório;
- **Mermaid** — modelagem dos fluxos de decisão;
- **Python** — implementação simplificada das regras;
- **Git/GitHub** — versionamento e disponibilização dos artefatos.

## 9. Organização da entrega

A solução está dividida em três componentes principais:

**1. Documentação funcional e técnica**

Descrição das regras, premissas, entradas, decisões, exceções e resultados esperados.

**2. Representação gráfica**

Fluxogramas das principais decisões envolvidas na parametrização.

**3. Implementação de referência**

Código simplificado demonstrando a tradução das regras de negócio para uma lógica computacional.

---

**Teste Técnico — Analista de Dados / Parametrização**

**Francinildo Vieira**
