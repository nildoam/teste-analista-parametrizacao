# Solução Técnica — Analista de Dados / Parametrização

## 1. Apresentação

Este documento apresenta a análise e a proposta de solução desenvolvida para o teste técnico de **Analista de Dados/Parametrização**.

A solução foi estruturada a partir da interpretação dos requisitos apresentados no teste, buscando transformar as regras funcionais em uma estrutura de parametrização clara, rastreável e passível de implementação.

O trabalho considera não apenas o resultado esperado de cada regra, mas também as condições necessárias para sua aplicação, possíveis exceções, dados de entrada e pontos de decisão envolvidos no processamento.

A proposta está organizada em três perspectivas complementares:

- **funcional**, por meio da identificação e documentação das regras de negócio;
- **visual**, por meio de fluxogramas representando os principais pontos de decisão;
- **técnica**, por meio de pseudocódigo e de uma implementação simplificada das regras.

Essa separação busca facilitar a validação da solução tanto por profissionais responsáveis pelas regras de negócio quanto por profissionais responsáveis pela implementação tecnológica.

---

## 2. Objetivo

O objetivo desta solução é demonstrar uma abordagem estruturada para análise e parametrização das regras apresentadas no teste técnico.

Especificamente, pretende-se:

- identificar as informações necessárias para aplicação das regras;
- organizar as condições de decisão de maneira objetiva;
- separar regras gerais de situações excepcionais;
- representar as decisões por meio de matrizes e fluxogramas;
- permitir a rastreabilidade entre requisito, regra e resultado;
- demonstrar como as regras podem ser traduzidas para lógica computacional;
- facilitar futuras alterações de parâmetros sem necessidade de reestruturação completa da solução.

A implementação apresentada neste trabalho possui caráter de **prova de conceito**, tendo como foco principal demonstrar a correta interpretação e estruturação das regras de negócio.

---

## 3. Escopo da solução

A solução contempla a análise das regras apresentadas no teste, especialmente aquelas relacionadas ao tratamento previdenciário, tributário e às respectivas rubricas.

O escopo compreende:

- identificação do enquadramento aplicável;
- diferenciação entre os regimes previdenciários previstos;
- avaliação das incidências associadas às rubricas;
- tratamento das condições relacionadas ao IRRF;
- definição dos resultados esperados para cada combinação relevante;
- identificação de exceções;
- representação gráfica das decisões;
- elaboração de pseudocódigo;
- implementação simplificada da lógica para fins demonstrativos.

Não faz parte do escopo desenvolver um sistema completo de folha de pagamento ou reproduzir integralmente todas as funcionalidades de um sistema de gestão de pessoal.

A implementação técnica tem como finalidade validar a estrutura lógica das regras definidas neste documento.

---

## 4. Premissas

Para elaboração da solução foram consideradas as seguintes premissas:

1. As informações e regras fornecidas no teste técnico constituem a principal referência funcional para a solução.

2. As regras devem ser tratadas de forma parametrizável sempre que possível, evitando valores ou comportamentos desnecessariamente fixados no código.

3. Cada decisão relevante deve possuir condições de entrada claramente identificadas e um resultado esperado.

4. Regras gerais e exceções devem ser documentadas separadamente, permitindo identificar facilmente quando uma condição específica altera o comportamento padrão.

5. A solução deve permitir rastrear a relação entre:
   
   **entrada → condição → regra aplicada → resultado.**

6. Alterações futuras em parâmetros, alíquotas, limites ou regras devem causar o menor impacto possível na estrutura da solução.

7. Os fluxogramas representam visualmente as mesmas regras descritas na documentação, não constituindo regras independentes.

8. O código apresentado no repositório constitui uma implementação de referência e não substitui as validações necessárias para utilização em ambiente de produção.

---

## 5. Dados de entrada

A definição das regras de parametrização parte das informações cadastrais e funcionais disponíveis para cada servidor.

Esses dados são utilizados para identificar o vínculo vigente, o enquadramento previdenciário aplicável e as condições necessárias para o lançamento das respectivas rubricas de desconto.

### 5.1 Informações necessárias

| Informação | Finalidade na parametrização |
|---|---|
| Identificação do servidor | Identificar o registro funcional submetido ao processamento |
| Regime de trabalho | Determinar o enquadramento funcional do servidor |
| Regime previdenciário | Determinar se a contribuição será destinada ao RGPS ou RPPS |
| Situação do vínculo | Verificar se o vínculo está vigente na competência processada |
| Data de início do vínculo | Determinar a partir de qual competência a regra poderá ser aplicada |
| Data de término do vínculo | Determinar até qual competência a regra permanece aplicável |
| Situação de atividade | Diferenciar situações como servidor ativo e inativo/aposentado |
| Condição de isenção de IRRF | Identificar servidores para os quais não deverá ocorrer retenção de Imposto de Renda |
| Competência da folha | Determinar o período de referência utilizado na avaliação das regras |
| Existência de rendimento tributável | Determinar a aplicabilidade da regra de IRRF |

### 5.2 Regimes de trabalho identificados

Conforme os cenários apresentados no teste, os vínculos funcionais devem ser classificados considerando os seguintes regimes de trabalho:

- estatutário;
- servidor público civil;
- servidor público militar;
- servidor comissionado;
- temporário;
- prestador de serviços.

A classificação do regime de trabalho constitui uma das principais entradas da parametrização, pois influencia diretamente a identificação da regra previdenciária aplicável.

### 5.3 Agrupamento para tratamento previdenciário

Para fins da solução proposta, os regimes são agrupados conforme a forma de contribuição previdenciária.

> **Premissa de parametrização:** os agrupamentos apresentados a seguir representam a interpretação funcional adotada para a solução do teste. Em uma implantação real, o enquadramento previdenciário deverá ser confirmado pelos dados cadastrais e pelas regras legais/configurações vigentes de cada vínculo.

#### RGPS — Regime Geral de Previdência Social

São tratados no grupo de contribuição ao RGPS os vínculos enquadrados, conforme as condições do teste, como:

- servidor comissionado sem vínculo efetivo;
- servidor temporário;
- prestador de serviços pessoa física / contribuinte individual.

Nesses casos, quando atendidas as demais condições de vigência e incidência, deverá ser avaliado o lançamento da rubrica correspondente à contribuição previdenciária do **RGPS/INSS**.

#### RPPS — Regime Próprio de Previdência Social

São tratados no grupo de contribuição ao RPPS os servidores cujo vínculo efetivo esteja submetido ao regime próprio, incluindo os enquadramentos funcionais aplicáveis a:

- servidor estatutário;
- servidor público civil efetivo.

Quando atendidas as condições necessárias, deverá ser avaliado o lançamento da rubrica correspondente à **contribuição previdenciária do RPPS**.

#### Servidor público militar

O servidor público militar deve ser tratado separadamente dos grupos anteriores.

Embora possua natureza previdenciária própria, não presumir seu enquadramento em RGPS ou RPPS sem a identificação do regime previdenciário aplicável ao vínculo. A solução deverá preservar essa distinção para permitir tratamento específico conforme as regras definidas para esse regime.

### 5.4 Informações utilizadas na decisão de IRRF

A regra de Imposto de Renda deve ser avaliada independentemente da classificação previdenciária.

Assim, um servidor enquadrado no RGPS ou no RPPS poderá também estar sujeito à rubrica de IRRF, desde que sejam satisfeitas as condições tributárias correspondentes.

Para essa decisão deverão ser consideradas, no mínimo:

- existência de rendimento sujeito à tributação;
- vigência do vínculo na competência processada;
- situação funcional do servidor;
- existência ou não de condição de isenção de Imposto de Renda.

Uma exceção relevante apresentada no teste corresponde aos **servidores inativos ou aposentados que possuam isenção de Imposto de Renda**.

Nessa situação, a condição de isenção deverá impedir o lançamento da rubrica de IRRF enquanto estiver vigente.

### 5.5 Competência e vigência

As regras deverão considerar a competência da folha em relação às datas de vigência das informações cadastrais.

De forma conceitual, uma condição será considerada vigente quando a competência processada estiver compreendida entre sua data de início e sua data de término.

Quando não existir data de término, a condição será considerada vigente a partir da data inicial enquanto não houver registro que determine seu encerramento.

A avaliação pode ser representada conceitualmente por:

```text id="dduea4"
VIGENTE =
    data_inicio <= competencia
    E
    (data_fim não informada OU data_fim >= competencia)
```

Esse padrão poderá ser reutilizado para vínculos e demais condições cadastrais que possuam período de validade.

### 5.6 Dados derivados

A partir dos dados de entrada, a solução poderá produzir informações derivadas utilizadas pelas regras posteriores:

| Informação derivada | Resultado esperado |
|---|---|
| `vinculo_vigente` | Verdadeiro/Falso |
| `grupo_previdenciario` | RGPS / RPPS / MILITAR / NÃO APLICÁVEL |
| `possui_isencao_irrf` | Verdadeiro/Falso |
| `aplica_contribuicao_rgps` | Verdadeiro/Falso |
| `aplica_contribuicao_rpps` | Verdadeiro/Falso |
| `aplica_irrf` | Verdadeiro/Falso |

Essa separação permite que os dados cadastrais sejam inicialmente interpretados e posteriormente utilizados pelas regras de lançamento das rubricas.

---

## 6. Regras de negócio

A partir dos dados de entrada definidos anteriormente, as regras de negócio deverão determinar **quais rubricas de desconto são aplicáveis a cada servidor em determinada competência**.

### Quantidade de rubricas propostas

Para atendimento das regras apresentadas no teste, propõe-se inicialmente a criação de **3 rubricas de desconto**:

1. **IRRF — Imposto de Renda Retido na Fonte**;
2. **RGPS/INSS — Contribuição Previdenciária do Regime Geral**;
3. **RPPS — Contribuição Previdenciária do Regime Próprio**.

A quantidade proposta considera o agrupamento dos servidores que compartilham a mesma natureza de desconto e a mesma lógica geral de incidência, evitando a criação desnecessária de rubricas distintas para cada regime de trabalho.

A solução considera inicialmente três grupos principais de rubricas:

| Código lógico | Rubrica | Finalidade |
|---|---|---|
| `IRRF` | Imposto de Renda Retido na Fonte | Registrar a retenção de Imposto de Renda quando aplicável |
| `RGPS` | Contribuição Previdenciária — RGPS/INSS | Registrar a contribuição do servidor vinculado ao Regime Geral |
| `RPPS` | Contribuição Previdenciária — RPPS | Registrar a contribuição do servidor vinculado ao Regime Próprio |

A definição dessas rubricas representa a estrutura mínima necessária para atender aos cenários previdenciários e tributários apresentados no teste.

O tratamento do regime militar será mantido separado até a definição de sua regra específica, evitando classificá-lo incorretamente como RGPS ou RPPS civil.

---

### 6.1 Regra de enquadramento previdenciário

Antes de determinar qual rubrica previdenciária deverá ser lançada, a solução deve identificar o enquadramento previdenciário correspondente ao vínculo do servidor.

A avaliação deverá ocorrer somente para vínculos vigentes na competência processada.

#### Condições

1. Identificar o vínculo funcional do servidor.
2. Verificar se o vínculo está vigente na competência.
3. Identificar o regime de trabalho.
4. Identificar o regime previdenciário associado ao vínculo.
5. Classificar o servidor em um dos grupos previdenciários previstos.

#### Decisão

```text
SE vínculo não estiver vigente
    grupo_previdenciario = NÃO_APLICÁVEL

SENÃO SE regime possuir enquadramento no RGPS
    grupo_previdenciario = RGPS

SENÃO SE regime possuir enquadramento no RPPS
    grupo_previdenciario = RPPS

SENÃO SE regime corresponder ao regime militar
    grupo_previdenciario = MILITAR

SENÃO
    grupo_previdenciario = NÃO_IDENTIFICADO
```

#### Resultado

A regra deverá produzir uma classificação previdenciária que será utilizada pelas regras posteriores:

- `RGPS`;
- `RPPS`;
- `MILITAR`;
- `NÃO_APLICÁVEL`;
- `NÃO_IDENTIFICADO`.

A utilização de `NÃO_IDENTIFICADO` é importante para impedir que um cadastro não reconhecido seja automaticamente enquadrado em um regime previdenciário incorreto.

---

### 6.2 Regra de contribuição ao RGPS/INSS

A rubrica de contribuição ao RGPS deverá ser avaliada para os vínculos enquadrados no Regime Geral de Previdência Social.

Entre os cenários identificados estão:

- servidor comissionado sem vínculo efetivo;
- servidor temporário;
- prestador de serviços pessoa física / contribuinte individual.

#### Condições

Para aplicação da regra deverão ser satisfeitas as seguintes condições:

- o vínculo deve estar vigente na competência;
- o enquadramento previdenciário deve corresponder ao `RGPS`;
- o vínculo deve possuir condição de incidência previdenciária;
- não deverá existir condição cadastral que impeça a aplicação da contribuição.

#### Decisão

```text
SE vinculo_vigente = VERDADEIRO
   E grupo_previdenciario = RGPS
   E possui_incidencia_previdenciaria = VERDADEIRO

ENTÃO
   aplica_contribuicao_rgps = VERDADEIRO

SENÃO
   aplica_contribuicao_rgps = FALSO
```

#### Resultado

Quando o resultado for verdadeiro, deverá ser gerado o lançamento lógico da rubrica:

```text
CONTRIBUIÇÃO PREVIDENCIÁRIA — RGPS/INSS
```

A regra determina a **aplicabilidade da rubrica**, não o seu valor financeiro. Alíquotas, limites e demais elementos de cálculo deverão ser tratados como parâmetros específicos do processo de cálculo.

---

### 6.3 Regra de contribuição ao RPPS

A rubrica de contribuição ao RPPS deverá ser avaliada para servidores cujo vínculo efetivo esteja submetido ao Regime Próprio de Previdência Social.

#### Condições

Para aplicação da regra deverão ser satisfeitas as seguintes condições:

- o vínculo deve estar vigente;
- o servidor deve possuir vínculo efetivo sujeito ao regime próprio;
- o enquadramento previdenciário deve corresponder ao `RPPS`;
- deverá existir incidência previdenciária para a situação processada.

#### Decisão

```text
SE vinculo_vigente = VERDADEIRO
   E grupo_previdenciario = RPPS
   E possui_incidencia_previdenciaria = VERDADEIRO

ENTÃO
   aplica_contribuicao_rpps = VERDADEIRO

SENÃO
   aplica_contribuicao_rpps = FALSO
```

#### Resultado

Quando satisfeitas as condições, deverá ser gerado o lançamento lógico da rubrica:

```text
CONTRIBUIÇÃO PREVIDENCIÁRIA — RPPS
```

Assim como na regra do RGPS, o cálculo financeiro não integra esta decisão. A parametrização determina inicialmente se a rubrica deverá ou não participar do processamento.

---

### 6.4 Regra de IRRF

A avaliação da rubrica de IRRF deverá ocorrer independentemente da classificação previdenciária.

Dessa forma, um servidor enquadrado no RGPS ou RPPS poderá também possuir incidência de IRRF, desde que as condições tributárias correspondentes sejam satisfeitas.

#### Condições

Para aplicação da regra deverão ser avaliadas:

- vigência do vínculo na competência;
- existência de rendimento sujeito à tributação;
- situação funcional do servidor;
- existência de condição de isenção de IRRF;
- vigência da eventual condição de isenção.

#### Regra geral

```text
SE vinculo_vigente = VERDADEIRO
   E possui_rendimento_tributavel = VERDADEIRO
   E possui_isencao_irrf = FALSO

ENTÃO
   aplica_irrf = VERDADEIRO

SENÃO
   aplica_irrf = FALSO
```

#### Exceção — servidor inativo/aposentado com isenção

Quando o servidor estiver enquadrado como inativo ou aposentado e possuir condição válida de isenção de Imposto de Renda, a rubrica de IRRF não deverá ser lançada enquanto a isenção permanecer vigente.

```text
SE situacao_funcional = INATIVO_OU_APOSENTADO
   E possui_isencao_irrf = VERDADEIRO
   E isencao_vigente = VERDADEIRO

ENTÃO
   aplica_irrf = FALSO
```

#### Resultado

Quando `aplica_irrf = VERDADEIRO`, deverá ser gerado o lançamento lógico da rubrica:

```text
IRRF — IMPOSTO DE RENDA RETIDO NA FONTE
```

Quando houver condição válida de isenção, a ausência do lançamento deverá ser rastreável até a regra que provocou a não incidência.

---

### 6.5 Regra de tratamento do regime militar

O regime militar deverá permanecer separado do tratamento previdenciário aplicado aos regimes RGPS e RPPS civil.

#### Decisão

```text
SE grupo_previdenciario = MILITAR

ENTÃO
   NÃO lançar automaticamente rubrica RGPS
   NÃO lançar automaticamente rubrica RPPS
   encaminhar para regra previdenciária específica
```

Essa separação evita que uma classificação não contemplada pelas regras gerais produza lançamento previdenciário indevido.

---

### 6.6 Ordem de avaliação das regras

Para tornar o processamento previsível, as regras deverão ser executadas em uma sequência lógica.

```text
1. Identificar servidor e vínculo
              ↓
2. Validar vigência do vínculo
              ↓
3. Identificar regime de trabalho
              ↓
4. Determinar grupo previdenciário
              ↓
5. Avaliar incidência previdenciária
              ↓
6. Determinar RGPS / RPPS / tratamento específico
              ↓
7. Avaliar condições de IRRF
              ↓
8. Avaliar exceções e isenções
              ↓
9. Gerar conjunto de rubricas aplicáveis
```

A saída do processamento não deverá ser necessariamente uma única rubrica. Um mesmo servidor poderá possuir, por exemplo, uma rubrica previdenciária e uma rubrica tributária na mesma competência.

---

## 7. Matrizes de decisão

As regras anteriores podem ser consolidadas em matrizes de decisão para facilitar sua validação funcional.

### 7.1 Matriz previdenciária inicial

| Situação | Vínculo vigente | Grupo previdenciário | Resultado |
|---|---:|---|---|
| Comissionado sem vínculo efetivo | Sim | RGPS | Avaliar rubrica RGPS |
| Temporário | Sim | RGPS | Avaliar rubrica RGPS |
| Prestador PF / contribuinte individual | Sim | RGPS | Avaliar rubrica RGPS |
| Servidor efetivo sujeito ao regime próprio | Sim | RPPS | Avaliar rubrica RPPS |
| Servidor militar | Sim | MILITAR | Aplicar tratamento específico |
| Qualquer vínculo encerrado | Não | NÃO APLICÁVEL | Não lançar contribuição referente ao vínculo |
| Regime não reconhecido | Sim | NÃO IDENTIFICADO | Não lançar automaticamente e sinalizar para análise |

### 7.2 Matriz inicial de IRRF

| Vínculo vigente | Rendimento tributável | Isenção vigente | Resultado |
|---:|---:|---:|---|
| Sim | Sim | Não | Avaliar/Lançar IRRF |
| Sim | Sim | Sim | Não lançar IRRF |
| Sim | Não | Não | Não lançar IRRF |
| Não | — | — | Não lançar IRRF |

### 7.3 Combinação das decisões

As decisões previdenciárias e tributárias devem ser independentes.

Por exemplo:

| Cenário | Previdência | IRRF | Resultado lógico |
|---|---|---|---|
| Servidor RGPS sujeito a IRRF | RGPS | Sim | RGPS + IRRF |
| Servidor RGPS isento de IRRF | RGPS | Não | RGPS |
| Servidor RPPS sujeito a IRRF | RPPS | Sim | RPPS + IRRF |
| Servidor RPPS isento de IRRF | RPPS | Não | RPPS |
| Vínculo não vigente | Não aplicável | Não | Nenhuma rubrica decorrente do vínculo |

Essa separação evita criar uma regra única excessivamente complexa e permite que cada domínio seja alterado ou validado de forma independente.

## 8. Tratamento de exceções

A parametrização deve prever situações em que os dados cadastrais sejam insuficientes, inconsistentes ou incompatíveis com as regras definidas.

Como princípio de segurança, uma condição não identificada não deverá resultar automaticamente no lançamento de uma rubrica de desconto.

Nesses casos, a ocorrência deverá ser identificada e disponibilizada para análise, permitindo sua rastreabilidade e posterior correção.

### 8.1 Vínculo não vigente

Quando o vínculo não estiver vigente na competência processada, as regras associadas a esse vínculo não deverão produzir lançamentos.

```text
SE vinculo_vigente = FALSO

ENTÃO
    não gerar rubrica previdenciária decorrente do vínculo
    não gerar IRRF decorrente do vínculo
```

O encerramento do vínculo, portanto, funciona como uma condição anterior às demais avaliações.

---

### 8.2 Regime previdenciário não identificado

Caso as informações cadastrais não permitam determinar o enquadramento previdenciário, o sistema não deverá presumir automaticamente RGPS ou RPPS.

```text
SE grupo_previdenciario = NÃO_IDENTIFICADO

ENTÃO
    não lançar RGPS automaticamente
    não lançar RPPS automaticamente
    registrar ocorrência para análise
```

Essa abordagem reduz o risco de geração de desconto previdenciário incorreto em decorrência de cadastro incompleto ou inconsistente.

---

### 8.3 Informações cadastrais obrigatórias ausentes

A ausência de informações essenciais deverá impedir a aplicação automática das regras que dependam desses dados.

São exemplos:

- ausência do regime de trabalho;
- ausência do regime previdenciário quando necessário;
- ausência das informações necessárias para determinar a vigência;
- situação funcional não reconhecida;
- dados incompatíveis entre vínculo e regime.

A ocorrência deverá ser identificada para correção cadastral antes da aplicação da respectiva regra.

---

### 8.4 Informações cadastrais conflitantes

Quando duas ou mais informações produzirem enquadramentos incompatíveis, a parametrização não deverá escolher silenciosamente uma delas.

Exemplo conceitual:

```text
regime_trabalho = TEMPORÁRIO
regime_previdenciario = RPPS
```

Caso essa combinação não seja válida segundo as regras estabelecidas, o registro deverá ser classificado como inconsistente.

```text
SE dados_cadastrais_conflitantes = VERDADEIRO

ENTÃO
    suspender decisão automática dependente do conflito
    registrar inconsistência
    encaminhar para validação
```

---

### 8.5 Isenção de IRRF fora da vigência

A existência de um registro histórico de isenção não significa necessariamente que a condição seja válida na competência processada.

A regra deverá considerar seu período de vigência.

```text
SE possui_registro_isencao = VERDADEIRO
   E isencao_vigente = FALSO

ENTÃO
    tratar servidor como não isento na competência
```

Dessa forma, somente uma condição válida no período processado poderá impedir o lançamento da rubrica de IRRF.

---

### 8.6 Servidor inativo ou aposentado sem isenção

A situação de inatividade ou aposentadoria, isoladamente, não deverá ser interpretada como isenção automática de IRRF.

```text
SE situacao_funcional = INATIVO_OU_APOSENTADO
   E possui_isencao_irrf = FALSO

ENTÃO
    continuar avaliação normal da regra de IRRF
```

Assim, a exceção deverá depender explicitamente da existência e vigência da condição de isenção.

---

### 8.7 Regime militar

O enquadramento militar não deverá ser convertido automaticamente em RGPS ou RPPS civil.

```text
SE grupo_previdenciario = MILITAR

ENTÃO
    não aplicar regra RGPS
    não aplicar regra RPPS civil
    direcionar para tratamento previdenciário específico
```

A separação evita que uma regra genérica produza resultado incompatível com o regime identificado.

---

### 8.8 Falha segura

Como princípio geral da solução, situações não reconhecidas deverão adotar comportamento de **falha segura**.

Isso significa que:

> uma condição desconhecida ou inconsistente não deverá gerar automaticamente uma rubrica de desconto.

A ocorrência deverá ser registrada para análise, contendo, sempre que possível:

- identificação do servidor;
- competência;
- vínculo;
- regra avaliada;
- condição encontrada;
- resultado da validação;
- motivo do impedimento.

Essa estratégia permite auditoria e facilita a identificação de problemas cadastrais ou de parametrização.

---

## 9. Fluxos de decisão

As regras descritas anteriormente serão representadas graficamente para facilitar sua validação e compreensão.

Foram definidos dois fluxos principais:

1. **Fluxo de enquadramento e contribuição previdenciária** — responsável por determinar RGPS, RPPS, regime militar ou situações que exijam análise.

2. **Fluxo de decisão do IRRF** — responsável por avaliar vigência, rendimento tributável e condições de isenção.

Os diagramas serão mantidos no diretório:

```text
docs/diagramas/
```

Além da representação gráfica, os respectivos arquivos-fonte serão mantidos no repositório para permitir manutenção e versionamento dos fluxos.

## 10. Pseudocódigo

O pseudocódigo a seguir representa a tradução das regras funcionais para uma sequência lógica de processamento.

Seu objetivo é demonstrar a implementação conceitual das regras sem vinculá-las a uma linguagem de programação específica.

### 10.1 Processamento principal

O processamento recebe como entradas os dados do servidor e a competência da folha e retorna o conjunto de rubricas aplicáveis.

```text id="w0l3c2"
FUNÇÃO PROCESSAR_SERVIDOR(servidor, competencia)

    rubricas = lista vazia
    ocorrencias = lista vazia

    SE NÃO VINCULO_VIGENTE(servidor, competencia)
        RETORNAR rubricas, ocorrencias
    FIM SE

    grupo_previdenciario =
        IDENTIFICAR_GRUPO_PREVIDENCIARIO(servidor)

    SE grupo_previdenciario = RGPS

        SE POSSUI_INCIDENCIA_PREVIDENCIARIA(servidor)
            ADICIONAR "RGPS" EM rubricas
        FIM SE

    SENÃO SE grupo_previdenciario = RPPS

        SE POSSUI_INCIDENCIA_PREVIDENCIARIA(servidor)
            ADICIONAR "RPPS" EM rubricas
        FIM SE

    SENÃO SE grupo_previdenciario = MILITAR

        ADICIONAR
            "TRATAMENTO_PREVIDENCIARIO_ESPECIFICO"
            EM ocorrencias

    SENÃO

        ADICIONAR
            "REGIME_PREVIDENCIARIO_NAO_IDENTIFICADO"
            EM ocorrencias

    FIM SE

    SE APLICAR_IRRF(servidor, competencia)
        ADICIONAR "IRRF" EM rubricas
    FIM SE

    RETORNAR rubricas, ocorrencias

FIM FUNÇÃO
```

O processamento retorna separadamente:

- **rubricas**, contendo os lançamentos identificados pelas regras;
- **ocorrências**, contendo situações que necessitam de tratamento ou validação.

Essa separação evita transformar inconsistências cadastrais em lançamentos financeiros.

---

### 10.2 Validação da vigência do vínculo

```text id="jhd9y8"
FUNÇÃO VINCULO_VIGENTE(servidor, competencia)

    SE servidor.data_inicio > competencia
        RETORNAR FALSO
    FIM SE

    SE servidor.data_fim EXISTIR
       E servidor.data_fim < competencia

        RETORNAR FALSO
    FIM SE

    RETORNAR VERDADEIRO

FIM FUNÇÃO
```

A ausência de data final representa um vínculo ainda vigente, desde que sua data inicial seja anterior ou igual à competência processada.

---

### 10.3 Identificação do grupo previdenciário

```text id="96rxfo"
FUNÇÃO IDENTIFICAR_GRUPO_PREVIDENCIARIO(servidor)

    SE servidor.regime = COMISSIONADO_SEM_VINCULO
        RETORNAR RGPS

    SENÃO SE servidor.regime = TEMPORARIO
        RETORNAR RGPS

    SENÃO SE servidor.regime = PRESTADOR_PF
        RETORNAR RGPS

    SENÃO SE servidor.regime = EFETIVO_RPPS
        RETORNAR RPPS

    SENÃO SE servidor.regime = MILITAR
        RETORNAR MILITAR

    SENÃO
        RETORNAR NÃO_IDENTIFICADO

    FIM SE

FIM FUNÇÃO
```

Na implementação definitiva, essas correspondências devem preferencialmente ser mantidas como parâmetros, evitando que novas classificações exijam alteração estrutural do algoritmo.

---

### 10.4 Avaliação da contribuição previdenciária

A incidência previdenciária funciona como condição adicional ao enquadramento.

```text id="1tmkfn"
FUNÇÃO POSSUI_INCIDENCIA_PREVIDENCIARIA(servidor)

    SE servidor.incidencia_previdenciaria = VERDADEIRO
        RETORNAR VERDADEIRO
    SENÃO
        RETORNAR FALSO
    FIM SE

FIM FUNÇÃO
```

Assim, identificar o servidor como pertencente ao RGPS ou RPPS não significa, isoladamente, gerar uma rubrica. As demais condições da parametrização ainda devem ser satisfeitas.

---

### 10.5 Avaliação do IRRF

```text id="9c4p47"
FUNÇÃO APLICAR_IRRF(servidor, competencia)

    SE NÃO VINCULO_VIGENTE(servidor, competencia)
        RETORNAR FALSO
    FIM SE

    SE servidor.possui_rendimento_tributavel = FALSO
        RETORNAR FALSO
    FIM SE

    SE POSSUI_ISENCAO_IRRF_VIGENTE(servidor, competencia)
        RETORNAR FALSO
    FIM SE

    RETORNAR VERDADEIRO

FIM FUNÇÃO
```

A situação funcional poderá participar da identificação da condição de isenção, mas a condição de aposentado ou inativo não deverá, isoladamente, impedir o IRRF.

---

### 10.6 Validação da isenção de IRRF

```text id="twzjn8"
FUNÇÃO POSSUI_ISENCAO_IRRF_VIGENTE(servidor, competencia)

    SE servidor.possui_isencao_irrf = FALSO
        RETORNAR FALSO
    FIM SE

    SE servidor.data_inicio_isencao > competencia
        RETORNAR FALSO
    FIM SE

    SE servidor.data_fim_isencao EXISTIR
       E servidor.data_fim_isencao < competencia

        RETORNAR FALSO
    FIM SE

    RETORNAR VERDADEIRO

FIM FUNÇÃO
```

Essa validação impede que um registro histórico de isenção seja utilizado fora de seu período de validade.

---

### 10.7 Resultado do processamento

Considere, conceitualmente, um servidor com:

```text id="n02ms3"
regime = EFETIVO_RPPS
vinculo_vigente = VERDADEIRO
incidencia_previdenciaria = VERDADEIRO
possui_rendimento_tributavel = VERDADEIRO
possui_isencao_irrf = FALSO
```

O processamento deverá produzir:

```text id="2fmq1x"
rubricas = [
    "RPPS",
    "IRRF"
]

ocorrencias = []
```

Em outro cenário:

```text id="0a90yu"
regime = REGIME_DESCONHECIDO
vinculo_vigente = VERDADEIRO
```

o resultado previdenciário deverá ser:

```text id="hruocb"
rubricas = []

ocorrencias = [
    "REGIME_PREVIDENCIARIO_NAO_IDENTIFICADO"
]
```

A segunda situação demonstra o princípio de falha segura adotado na solução: a impossibilidade de identificar corretamente uma regra não deve produzir automaticamente uma rubrica de desconto.

---

## 11. Implementação de referência

As regras apresentadas no pseudocódigo serão traduzidas para uma implementação simplificada em Python.

O código será disponibilizado em:

```text id="8nyhhq"
src/regras_parametrizacao.py
```

A implementação terá caráter demonstrativo e deverá manter correspondência direta com as regras documentadas anteriormente.

A estrutura será dividida em funções responsáveis por:

- validar a vigência do vínculo;
- determinar o grupo previdenciário;
- validar a incidência previdenciária;
- avaliar a vigência da isenção de IRRF;
- determinar a aplicabilidade do IRRF;
- consolidar as rubricas aplicáveis;
- registrar situações que necessitem de análise.

Essa organização busca manter as responsabilidades separadas e facilitar testes e futuras alterações das regras.

## 12. Cenários de teste

Para validar a correspondência entre as regras documentadas e a implementação de referência, foram definidos cenários representativos do processamento.

Os testes automatizados estão disponíveis em:

```text
src/test_regras_parametrizacao.py
```

### 12.1 Matriz de cenários

| Cenário | Regime/Situação | Previdência | IRRF | Resultado esperado |
|---|---|---|---|---|
| 01 | Efetivo RPPS | Incide | Tributável e sem isenção | `RPPS + IRRF` |
| 02 | Temporário | Incide | Tributável e sem isenção | `RGPS + IRRF` |
| 03 | Comissionado sem vínculo efetivo | Incide | Isenção vigente | `RGPS` |
| 04 | Inativo/Aposentado com isenção | Conforme enquadramento | Isenção vigente | Sem `IRRF` |
| 05 | Vínculo encerrado | Não aplicável | Não aplicável | Nenhuma rubrica |
| 06 | Regime desconhecido | Não identificado | Não tributável no cenário | Ocorrência para análise |
| 07 | Militar | Tratamento específico | Não tributável no cenário | Ocorrência para tratamento específico |

### 12.2 Cenário 01 — Servidor efetivo RPPS

**Entrada principal:**

```text
regime = EFETIVO_RPPS
vínculo vigente = SIM
incidência previdenciária = SIM
rendimento tributável = SIM
isenção IRRF = NÃO
```

**Resultado esperado:**

```text
rubricas = [RPPS, IRRF]
ocorrencias = []
```

---

### 12.3 Cenário 02 — Servidor temporário

**Entrada principal:**

```text
regime = TEMPORARIO
vínculo vigente = SIM
incidência previdenciária = SIM
rendimento tributável = SIM
isenção IRRF = NÃO
```

**Resultado esperado:**

```text
rubricas = [RGPS, IRRF]
ocorrencias = []
```

---

### 12.4 Cenário 03 — RGPS com isenção de IRRF

O servidor permanece sujeito à contribuição previdenciária, porém possui condição válida de isenção tributária.

**Resultado esperado:**

```text
rubricas = [RGPS]
ocorrencias = []
```

Esse cenário demonstra a independência entre as regras previdenciária e tributária.

---

### 12.5 Cenário 04 — Inativo/Aposentado com isenção vigente

A situação de inatividade ou aposentadoria não representa, isoladamente, isenção automática.

Quando existir uma condição válida e vigente de isenção de IRRF, a rubrica tributária não deverá ser aplicada.

**Resultado esperado:**

```text
IRRF não aplicável
```

---

### 12.6 Cenário 05 — Vínculo encerrado

Quando a data final do vínculo for anterior à competência processada, nenhuma regra decorrente desse vínculo deverá produzir lançamento.

**Resultado esperado:**

```text
rubricas = []
ocorrencias = []
```

---

### 12.7 Cenário 06 — Regime não identificado

Quando o regime informado não puder ser associado a uma regra previdenciária conhecida, nenhuma contribuição previdenciária deverá ser presumida.

**Resultado esperado:**

```text
rubricas = []

ocorrencias = [
    REGIME_PREVIDENCIARIO_NAO_IDENTIFICADO
]
```

---

### 12.8 Cenário 07 — Regime militar

O regime militar não deverá ser automaticamente tratado pelas regras de RGPS ou RPPS civil.

**Resultado esperado:**

```text
rubricas = []

ocorrencias = [
    TRATAMENTO_PREVIDENCIARIO_ESPECIFICO
]
```

---

### 12.9 Critério de validação

Um cenário será considerado aprovado quando o conjunto de rubricas e ocorrências retornado pela implementação corresponder ao resultado definido na matriz de decisão.

Os testes automatizados permitem verificar essa correspondência sempre que a implementação for alterada.

A estratégia busca garantir a rastreabilidade:

```text
Regra de negócio
       ↓
Matriz de decisão
       ↓
Pseudocódigo
       ↓
Implementação
       ↓
Cenário de teste
       ↓
Resultado esperado
```
