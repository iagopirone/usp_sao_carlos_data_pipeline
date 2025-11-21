"""
Módulo de TRANSFORMAÇÃO
Limpa, padroniza e filtra os dados para o campus de São Carlos.
"""

import pandas as pd


def normalizar_colunas(df: pd.DataFrame) -> pd.DataFrame:
    """
    Deixa os nomes das colunas padronizados.
    """
    df = df.copy()
    df.columns = (
        df.columns.astype(str)
        .str.strip()
        .str.lower()
        .str.replace(r"\s+", "_", regex=True)
    )
    return df


def filtrar_sao_carlos(df: pd.DataFrame) -> pd.DataFrame:
    """
    Filtra apenas as linhas referentes ao campus de São Carlos.
    """
    if df is None:
        return None

    # algumas tabelas têm nomes diferentes
    possiveis_colunas = ["campus", "Campus", "unidade", "Unidade"]

    for col in possiveis_colunas:
        if col in df.columns:
            filtro = df[col].astype(str).str.contains("São Carlos", case=False, na=False)
            return df.loc[filtro].reset_index(drop=True)

    # caso não tenha coluna de campus
    return df


# A partir do notebook, todos os indicadores usam o mesmo padrão:
# carregar → filtrar São Carlos → salvar
# portanto, cada função aqui só encapsula isso.


def transformar_area_territorial(df_raw: pd.DataFrame) -> pd.DataFrame:
    df = normalizar_colunas(df_raw)
    df = filtrar_sao_carlos(df)
    return df


def transformar_infraestrutura(df_raw: pd.DataFrame) -> pd.DataFrame:
    df = normalizar_colunas(df_raw)
    df = filtrar_sao_carlos(df)
    return df


def transformar_servidores_tecnico_adm(df_raw: pd.DataFrame) -> pd.DataFrame:
    df = normalizar_colunas(df_raw)
    df = filtrar_sao_carlos(df)
    return df


def transformar_docentes(df_raw: pd.DataFrame) -> pd.DataFrame:
    df = normalizar_colunas(df_raw)
    df = filtrar_sao_carlos(df)
    return df


def transformar_graduacao_snapshot(df_raw: pd.DataFrame) -> pd.DataFrame:
    df = normalizar_colunas(df_raw)
    df = filtrar_sao_carlos(df)
    return df


def transformar_pos_capes_snapshot(df_raw: pd.DataFrame) -> pd.DataFrame:
    df = normalizar_colunas(df_raw)
    df = filtrar_sao_carlos(df)
    return df


def transformar_pos_evolucao(df_raw: pd.DataFrame) -> pd.DataFrame:
    df = normalizar_colunas(df_raw)
    df = filtrar_sao_carlos(df)
    return df


def transformar_extensao_distancia(df_raw: pd.DataFrame) -> pd.DataFrame:
    df = normalizar_colunas(df_raw)
    df = filtrar_sao_carlos(df)
    return df
