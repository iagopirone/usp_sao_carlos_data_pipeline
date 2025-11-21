"""
PIPELINE PRINCIPAL
Executa a extração → transformação → carga para todos os indicadores e anos.
"""

from extract import carregar_tabela_anuario_usp
from transform import (
    transformar_area_territorial,
    transformar_infraestrutura,
    transformar_servidores_tecnico_adm,
    transformar_docentes,
    transformar_graduacao_snapshot,
    transformar_pos_capes_snapshot,
    transformar_pos_evolucao,
    transformar_extensao_distancia,
)
from load import salvar_csv

# anos que você usou no notebook
ANOS = [2019, 2020, 2021, 2022, 2023, 2024]

# códigos de tabela retirados do notebook original
MAPA_TABELAS = {
    "area_territorial": "T1.06",
    "infraestrutura": "T1.07",
    "servidores_tecnico_adm": "T2.01",
    "docentes": "T2.09",
    "graduacao_snapshot": "T3.02",
    "pos_capes_snapshot": "T3.31",
    "pos_evolucao_historica": "T3.33",
    "extensao_distancia": "T3.35",
}


def executar_pipeline():
    """
    Executa todo o pipeline de dados para todos os indicadores e anos.
    """

    for ano in ANOS:
        print("\n" + "=" * 70)
        print(f"📅 Processando ano {ano}")
        print("=" * 70)

        # 1. Área Territorial
        df_raw = carregar_tabela_anuario_usp(ano, MAPA_TABELAS["area_territorial"])
        df_tratado = transformar_area_territorial(df_raw)
        salvar_csv(df_tratado, f"area_territorial_sao_carlos_{ano}.csv")

        # 2. Infraestrutura
        df_raw = carregar_tabela_anuario_usp(ano, MAPA_TABELAS["infraestrutura"])
        df_tratado = transformar_infraestrutura(df_raw)
        salvar_csv(df_tratado, f"infraestrutura_sao_carlos_{ano}.csv")

        # 3. Servidores Técnico-Administrativos
        df_raw = carregar_tabela_anuario_usp(ano, MAPA_TABELAS["servidores_tecnico_adm"])
        df_tratado = transformar_servidores_tecnico_adm(df_raw)
        salvar_csv(df_tratado, f"servidores_tecnico_adm_sao_carlos_{ano}.csv")

        # 4. Docentes
        df_raw = carregar_tabela_anuario_usp(ano, MAPA_TABELAS["docentes"])
        df_tratado = transformar_docentes(df_raw)
        salvar_csv(df_tratado, f"docentes_sao_carlos_{ano}.csv")

        # 5. Graduação (snapshot anual)
        df_raw = carregar_tabela_anuario_usp(ano, MAPA_TABELAS["graduacao_snapshot"])
        df_tratado = transformar_graduacao_snapshot(df_raw)
        salvar_csv(df_tratado, f"graduacao_snapshot_sao_carlos_{ano}.csv")

        # 6. Pós-graduação CAPES (snapshot anual)
        df_raw = carregar_tabela_anuario_usp(ano, MAPA_TABELAS["pos_capes_snapshot"])
        df_tratado = transformar_pos_capes_snapshot(df_raw)
        salvar_csv(df_tratado, f"pos_capes_snapshot_sao_carlos_{ano}.csv")

        # 7. Pós-graduação – evolução histórica
        df_raw = carregar_tabela_anuario_usp(ano, MAPA_TABELAS["pos_evolucao_historica"])
        df_tratado = transformar_pos_evolucao(df_raw)
        salvar_csv(df_tratado, f"pos_evolucao_historica_sao_carlos_{ano}.csv")

        # 8. Extensão a distância
        df_raw = carregar_tabela_anuario_usp(ano, MAPA_TABELAS["extensao_distancia"])
        df_tratado = transformar_extensao_distancia(df_raw)
        salvar_csv(df_tratado, f"extensao_distancia_sao_carlos_{ano}.csv")

    print("\n🎉 Pipeline finalizado com sucesso!")
