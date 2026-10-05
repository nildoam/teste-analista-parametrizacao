"""
Testes da implementação de referência das regras de parametrização.

Os cenários validam a correspondência entre as regras documentadas
e os resultados produzidos pela implementação.
"""

import unittest
from datetime import date

from regras_parametrizacao import processar_servidor


COMPETENCIA = date(2026, 10, 1)


def criar_servidor(**alteracoes):
    """
    Cria um servidor-base válido e permite alterar somente
    os atributos necessários para cada cenário de teste.
    """

    servidor = {
        "regime": "EFETIVO_RPPS",
        "situacao_funcional": "ATIVO",
        "data_inicio_vinculo": date(2020, 1, 1),
        "data_fim_vinculo": None,
        "incidencia_previdenciaria": True,
        "possui_rendimento_tributavel": True,
        "possui_isencao_irrf": False,
        "data_inicio_isencao": None,
        "data_fim_isencao": None,
    }

    servidor.update(alteracoes)

    return servidor


class TestRegrasParametrizacao(unittest.TestCase):

    def test_01_efetivo_rpps_com_irrf(self):
        """
        Servidor RPPS com incidência previdenciária,
        rendimento tributável e sem isenção.
        """

        servidor = criar_servidor()

        resultado = processar_servidor(
            servidor,
            COMPETENCIA,
        )

        self.assertEqual(
            resultado["rubricas"],
            ["RPPS", "IRRF"],
        )

        self.assertEqual(
            resultado["ocorrencias"],
            [],
        )

    def test_02_temporario_rgps_com_irrf(self):
        """
        Servidor temporário enquadrado no RGPS
        e sujeito ao IRRF.
        """

        servidor = criar_servidor(
            regime="TEMPORARIO"
        )

        resultado = processar_servidor(
            servidor,
            COMPETENCIA,
        )

        self.assertEqual(
            resultado["rubricas"],
            ["RGPS", "IRRF"],
        )

        self.assertEqual(
            resultado["ocorrencias"],
            [],
        )

    def test_03_rgps_com_isencao_irrf(self):
        """
        Servidor RGPS com isenção de IRRF vigente.
        A contribuição previdenciária permanece aplicável,
        mas o IRRF não deverá ser lançado.
        """

        servidor = criar_servidor(
            regime="COMISSIONADO_SEM_VINCULO",
            possui_isencao_irrf=True,
            data_inicio_isencao=date(2025, 1, 1),
            data_fim_isencao=None,
        )

        resultado = processar_servidor(
            servidor,
            COMPETENCIA,
        )

        self.assertEqual(
            resultado["rubricas"],
            ["RGPS"],
        )

        self.assertNotIn(
            "IRRF",
            resultado["rubricas"],
        )

    def test_04_aposentado_com_isencao_irrf(self):
        """
        Representa servidor aposentado/inativo com
        condição de isenção de IRRF vigente.

        A situação funcional não gera a isenção por si só;
        o resultado decorre da condição de isenção vigente.
        """

        servidor = criar_servidor(
            situacao_funcional="APOSENTADO",
            possui_isencao_irrf=True,
            data_inicio_isencao=date(2024, 1, 1),
            data_fim_isencao=None,
        )

        resultado = processar_servidor(
            servidor,
            COMPETENCIA,
        )

        self.assertNotIn(
            "IRRF",
            resultado["rubricas"],
        )

    def test_05_vinculo_encerrado(self):
        """
        Vínculo encerrado antes da competência.
        Nenhuma rubrica deverá ser produzida.
        """

        servidor = criar_servidor(
            data_fim_vinculo=date(2026, 9, 30)
        )

        resultado = processar_servidor(
            servidor,
            COMPETENCIA,
        )

        self.assertEqual(
            resultado["rubricas"],
            [],
        )

        self.assertEqual(
            resultado["ocorrencias"],
            [],
        )

    def test_06_regime_nao_identificado(self):
        """
        Regime não reconhecido não deverá gerar
        contribuição previdenciária automaticamente.
        """

        servidor = criar_servidor(
            regime="REGIME_DESCONHECIDO",
            possui_rendimento_tributavel=False,
        )

        resultado = processar_servidor(
            servidor,
            COMPETENCIA,
        )

        self.assertEqual(
            resultado["rubricas"],
            [],
        )

        self.assertIn(
            "REGIME_PREVIDENCIARIO_NAO_IDENTIFICADO",
            resultado["ocorrencias"],
        )

    def test_07_regime_militar(self):
        """
        O regime militar deverá ser direcionado
        para tratamento previdenciário específico.
        """

        servidor = criar_servidor(
            regime="MILITAR",
            possui_rendimento_tributavel=False,
        )

        resultado = processar_servidor(
            servidor,
            COMPETENCIA,
        )

        self.assertEqual(
            resultado["rubricas"],
            [],
        )

        self.assertIn(
            "TRATAMENTO_PREVIDENCIARIO_ESPECIFICO",
            resultado["ocorrencias"],
        )


if __name__ == "__main__":
    unittest.main()
