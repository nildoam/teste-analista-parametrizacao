# Diagramas da solução

Este diretório contém os diagramas utilizados para representar os principais fluxos de decisão da solução de parametrização.

Os arquivos `.mmd` correspondem aos arquivos-fonte dos diagramas e permitem sua manutenção e versionamento.

## 1. Fluxo de enquadramento previdenciário

O fluxo abaixo representa a identificação do enquadramento previdenciário e a decisão sobre a aplicabilidade das rubricas de RGPS ou RPPS.

```mermaid
flowchart TD

    A([Início]) --> B[Identificar servidor e vínculo]
    B --> C{Vínculo vigente<br/>na competência?}

    C -- Não --> D[Não gerar rubrica previdenciária]
    D --> Z([Fim])

    C -- Sim --> E[Identificar regime de trabalho<br/>e regime previdenciário]
    E --> F{Enquadramento<br/>identificado?}

    F -- Não --> G[Classificar como<br/>NÃO IDENTIFICADO]
    G --> H[Registrar ocorrência<br/>para análise]
    H --> Z

    F -- Sim --> I{Grupo previdenciário}

    I -- RGPS --> J{Possui incidência<br/>previdenciária?}
    J -- Sim --> K[Aplicar rubrica<br/>RGPS / INSS]
    J -- Não --> L[Não aplicar<br/>rubrica RGPS]
    K --> Z
    L --> Z

    I -- RPPS --> M{Possui incidência<br/>previdenciária?}
    M -- Sim --> N[Aplicar rubrica<br/>RPPS]
    M -- Não --> O[Não aplicar<br/>rubrica RPPS]
    N --> Z
    O --> Z

    I -- MILITAR --> P[Não aplicar automaticamente<br/>RGPS ou RPPS civil]
    P --> Q[Direcionar para regra<br/>previdenciária específica]
    Q --> Z
```

### Interpretação

O processamento segue quatro etapas principais:

1. validação da vigência do vínculo;
2. identificação do enquadramento previdenciário;
3. avaliação da incidência previdenciária;
4. determinação da rubrica aplicável.

Registros cujo enquadramento não possa ser determinado não produzem automaticamente uma rubrica previdenciária e devem ser encaminhados para análise.

O regime militar também permanece separado das regras gerais de RGPS e RPPS civil, permitindo tratamento específico.

---

## 2. Fluxo de decisão do IRRF

O fluxo de IRRF é independente do enquadramento previdenciário. Seu objetivo é determinar se a rubrica de Imposto de Renda deverá participar do processamento na competência analisada.

```mermaid
flowchart TD

    A([Início]) --> B[Identificar servidor e vínculo]
    B --> C{Vínculo vigente<br/>na competência?}

    C -- Não --> D[Não aplicar rubrica de IRRF]
    D --> Z([Fim])

    C -- Sim --> E{Possui rendimento<br/>tributável?}

    E -- Não --> F[Não aplicar rubrica de IRRF]
    F --> Z

    E -- Sim --> G{Servidor inativo<br/>ou aposentado?}

    G -- Não --> H{Possui outra condição<br/>válida de isenção?}
    H -- Não --> I[Aplicar rubrica de IRRF]
    H -- Sim --> J{Isenção vigente<br/>na competência?}

    G -- Sim --> K{Possui isenção<br/>de IRRF?}
    K -- Não --> I
    K -- Sim --> L{Isenção vigente<br/>na competência?}

    L -- Sim --> M[Não aplicar rubrica de IRRF]
    L -- Não --> I

    J -- Sim --> M
    J -- Não --> I

    I --> Z
    M --> Z
```

### Interpretação

A decisão de IRRF considera inicialmente a validade do vínculo e a existência de rendimento tributável.

A condição de servidor inativo ou aposentado não representa, isoladamente, uma isenção. Para impedir o lançamento da rubrica deverá existir uma condição de isenção aplicável e vigente na competência processada.

Dessa forma, a decisão pode resultar em:

- **aplicar IRRF**, quando existirem as condições de tributação e nenhuma isenção válida;
- **não aplicar IRRF**, quando não houver rendimento tributável ou existir isenção vigente;
- **não processar a regra**, quando o vínculo não estiver vigente.

---

## 3. Independência entre as decisões

Os dois fluxos devem ser avaliados de forma independente.

O enquadramento previdenciário determina a aplicabilidade das rubricas de contribuição previdenciária, enquanto o fluxo tributário determina a aplicabilidade da rubrica de IRRF.

Consequentemente, um mesmo servidor poderá produzir, por exemplo:

```text
RGPS + IRRF
RPPS + IRRF
RGPS
RPPS
Nenhuma rubrica
```

Essa separação reduz o acoplamento entre as regras e facilita a manutenção da parametrização.
