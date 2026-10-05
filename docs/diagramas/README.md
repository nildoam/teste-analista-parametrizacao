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
