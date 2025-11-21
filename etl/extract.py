"""
Módulo de EXTRAÇÃO
Baixa tabelas do Anuário Estatístico da USP diretamente do USP Digital.
"""

import io
import pandas as pd
import requests


def montar_url_tabela(ano: int, codigo_tabela: str) -> str:
    """
    Constrói a URL oficial da tabela no USP Digital.
    O código vem no formato 'T1.06', e o sistema usa 'T1_06' no arquivo.
    """
    codigo_limpo = codigo_tabela.replace(".", "_")
    return f"https://uspdigital.usp.br/anuario/Anuario{ano}/Tabela{codigo_limpo}.xls"


def carregar_tabela_anuario_usp(ano: int, codigo_tabela: str) -> pd.DataFrame:
    """
    Faz o download da tabela e devolve como DataFrame.
    """

    url = montar_url_tabela(ano, codigo_tabela)
    print(f"[EXTRAÇÃO] Baixando tabela {codigo_tabela} ({ano})")
    print(f"[EXTRAÇÃO] URL: {url}")

    try:
        resp = requests.get(url, timeout=60)
        resp.raise_for_status()
    except Exception as e:
        print(f"❌ Erro ao baixar a tabela {codigo_tabela}: {e}")
        return None

    try:
        df = pd.read_excel(io.BytesIO(resp.content))
        print(f"✅ Tabela {codigo_tabela} ({ano}) carregada. Linhas: {df.shape[0]}")
        return df
    except Exception as e:
        print(f"❌ Erro ao ler a tabela {codigo_tabela}: {e}")
        return None
