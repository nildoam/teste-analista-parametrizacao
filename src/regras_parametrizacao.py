"""
Implementação de referência das regras de parametrização.

Objetivo:
    Demonstrar a tradução das regras de negócio documentadas
    para uma lógica computacional simples e rastreável.

Observação:
    Esta implementação possui caráter demonstrativo e não
    contempla cálculo financeiro de rubricas.
"""

from datetime import date


# Grupos previdenciários
RGPS = "RGPS"
RPPS = "RPPS"
MILITAR = "MILITAR"
NAO_IDENTIFICADO = "NAO_IDENTIFICADO"


def periodo_vigente(data_inicio, data_fim, competencia):
    """
    Verifica se um período está vigente na competência informada.
    """

    if data_inicio is None:
        return False

    if data_inicio > competencia:
        return False

    if data_fim is not None and data_fim < competencia:
        return False

    return True


def vinculo_vigente(servidor, competencia):
    """
    Verifica se o vínculo do servidor está vigente.
    """

    return periodo_vigente(
        servidor.get("data_inicio_vinculo"),
        servidor.get("data_fim_vinculo"),
        competencia,
    )


def identificar_grupo_previdenciario(servidor):
    """
    Identifica o grupo previdenciário a partir do regime
    funcional informado.
    """

    regime = servidor.get("regime")

    regimes_rgps = {
        "COMISSIONADO_SEM_VINCULO",
        "TEMPORARIO",
        "PRESTADOR_PF",
    }

    regimes_rpps = {
        "EFETIVO_RPPS",
    }

    if regime in regimes_rgps:
        return RGPS

    if regime in regimes_rpps:
        return RPPS

    if regime == "MILITAR":
        return MILITAR

    return NAO_IDENTIFICADO


def possui_incidencia_previdenciaria(servidor):
    """
    Verifica se existe incidência previdenciária para
    a situação processada.
    """

    return servidor.get("incidencia_previdenciaria", False)


def possui_isencao_irrf_vigente(servidor, competencia):
    """
    Verifica se existe uma condição de isenção de IRRF
    vigente na competência.
    """

    if not servidor.get("possui_isencao_irrf", False):
        return False

    return periodo_vigente(
        servidor.get("data_inicio_isencao"),
        servidor.get("data_fim_isencao"),
        competencia,
    )


def aplicar_irrf(servidor, competencia):
    """
    Determina se a rubrica de IRRF deverá ser aplicada.
    """

    if not vinculo_vigente(servidor, competencia):
        return False

    if not servidor.get("possui_rendimento_tributavel", False):
        return False

    if possui_isencao_irrf_vigente(servidor, competencia):
        return False

    return True


def processar_servidor(servidor, competencia):
    """
    Processa as regras de parametrização e retorna
    as rubricas aplicáveis e eventuais ocorrências.
    """

    rubricas = []
    ocorrencias = []

    # 1. Validação da vigência do vínculo
    if not vinculo_vigente(servidor, competencia):
        return {
            "rubricas": rubricas,
            "ocorrencias": ocorrencias,
        }

    # 2. Identificação do grupo previdenciário
    grupo_previdenciario = identificar_grupo_previdenciario(servidor)

    # 3. Avaliação da contribuição previdenciária
    if grupo_previdenciario == RGPS:

        if possui_incidencia_previdenciaria(servidor):
            rubricas.append("RGPS")

    elif grupo_previdenciario == RPPS:

        if possui_incidencia_previdenciaria(servidor):
            rubricas.append("RPPS")

    elif grupo_previdenciario == MILITAR:

        ocorrencias.append(
            "TRATAMENTO_PREVIDENCIARIO_ESPECIFICO"
        )

    else:

        ocorrencias.append(
            "REGIME_PREVIDENCIARIO_NAO_IDENTIFICADO"
        )

    # 4. Avaliação independente do IRRF
    if aplicar_irrf(servidor, competencia):
        rubricas.append("IRRF")

    return {
        "rubricas": rubricas,
        "ocorrencias": ocorrencias,
    }


# ---------------------------------------------------------
# Exemplo de utilização
# ---------------------------------------------------------

if __name__ == "__main__":

    servidor_exemplo = {
        "regime": "EFETIVO_RPPS",
        "data_inicio_vinculo": date(2020, 1, 1),
        "data_fim_vinculo": None,
        "incidencia_previdenciaria": True,
        "possui_rendimento_tributavel": True,
        "possui_isencao_irrf": False,
        "data_inicio_isencao": None,
        "data_fim_isencao": None,
    }

    competencia = date(2026, 10, 1)

    resultado = processar_servidor(
        servidor_exemplo,
        competencia,
    )

    print(resultado)
