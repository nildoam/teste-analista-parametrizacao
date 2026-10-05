# Implementação de referência

Este diretório contém uma implementação simplificada das regras de negócio descritas na documentação técnica.

O código possui caráter demonstrativo e tem como objetivo evidenciar como as regras de parametrização podem ser traduzidas para uma lógica computacional organizada, legível e testável.

## Arquivos

### `regras_parametrizacao.py`

Contém a implementação das principais regras utilizadas na solução, incluindo:

- validação da vigência do vínculo;
- identificação do grupo previdenciário;
- avaliação da incidência previdenciária;
- validação da vigência da isenção de IRRF;
- decisão sobre aplicação do IRRF;
- determinação das rubricas aplicáveis;
- registro de ocorrências que necessitam de tratamento específico ou análise.

A função principal é:

```python
processar_servidor(servidor, competencia)
```

Ela recebe os dados funcionais necessários para avaliação das regras e retorna duas coleções:

```python
{
    "rubricas": [],
    "ocorrencias": []
}
```

`rubricas` representa os descontos identificados pelas regras de parametrização.

`ocorrencias` representa situações que não devem resultar automaticamente em uma rubrica e necessitam de tratamento específico ou análise.

---

### `test_regras_parametrizacao.py`

Contém os testes automatizados utilizados para validar os principais cenários definidos na documentação técnica.

Foram considerados sete cenários:

1. servidor efetivo enquadrado em RPPS, tributável e sem isenção;
2. servidor temporário enquadrado em RGPS, tributável e sem isenção;
3. vínculo enquadrado em RGPS com isenção de IRRF vigente;
4. servidor aposentado com isenção de IRRF vigente;
5. vínculo encerrado antes da competência;
6. regime previdenciário não identificado;
7. servidor militar com tratamento previdenciário específico.

---

## Executando o exemplo

A partir da raiz do repositório:

```bash
python src/regras_parametrizacao.py
```

Para o exemplo disponibilizado no código, o resultado esperado é:

```text
{
    'rubricas': ['RPPS', 'IRRF'],
    'ocorrencias': []
}
```

---

## Executando os testes

A partir da raiz do repositório:

```bash
python -m unittest src.test_regras_parametrizacao
```

Resultado esperado:

```text
.......
----------------------------------------------------------------------
Ran 7 tests

OK
```

O tempo apresentado em `Ran 7 tests` pode variar de acordo com o ambiente de execução.

---

## Organização da lógica

A implementação segue, de forma simplificada, esta sequência:

```text
Dados do servidor
       │
       ▼
Vigência do vínculo
       │
       ▼
Grupo previdenciário
       │
       ├── RGPS
       ├── RPPS
       ├── Militar
       └── Não identificado
       │
       ▼
Incidência previdenciária
       │
       ▼
Avaliação independente do IRRF
       │
       ▼
Rubricas + Ocorrências
```

A separação entre a decisão previdenciária e a decisão tributária permite que diferentes combinações de rubricas sejam produzidas sem acoplamento entre as duas regras.

---

## Escopo da implementação

Esta implementação é uma **prova de conceito**.

Seu objetivo é demonstrar a tradução das regras funcionais para lógica computacional e não implementar um sistema completo de folha de pagamento.

Por esse motivo, não são tratados neste código:

- valores financeiros;
- alíquotas;
- faixas progressivas;
- bases de cálculo;
- persistência em banco de dados;
- interfaces;
- integrações externas.

Esses elementos poderiam ser incorporados posteriormente sem alterar o princípio de separação das regras adotado nesta solução.

---

## Documentação relacionada

A especificação completa das regras está disponível em:

[`docs/solucao-parametrizacao.md`](../docs/solucao-parametrizacao.md)

Os fluxos de decisão estão disponíveis em:

[`docs/diagramas/README.md`](../docs/diagramas/README.md)
