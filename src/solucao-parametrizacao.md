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

Embora possua natureza previdenciária própria, seu enquadramento não deve ser automaticamente tratado como RGPS ou RPPS civil. A solução deverá preservar essa distinção para permitir tratamento específico conforme as regras definidas para esse regime.

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

A solução considera inicialmente três grupos principais de rubricas:

| Código lógico | Rubrica | Finalidade |
|---|---|---|
| `IRRF` | Imposto de Renda Retido na Fonte | Registrar a retenção de Imposto de Renda quando aplicável |
| `RGPS` | Contribuição Previdenciária — RGPS/INSS | Registrar a contribuição do servidor vinculado ao Regime Geral |
| `RPPS` | Contribuição Previdenciária — RPPS | Registrar a contribuição do servidor vinculado ao Regime Próprio |

A definição dessas rubricas representa a estrutura mínima necessária para atender aos cenários previdenciários e tributários apresentados no teste.

O tratamento do regime militar será mantido separado até a definição de sua regra específica, evitando classificá-lo incorretamente como RGPS ou RPPS civil.
