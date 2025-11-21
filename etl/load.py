"""
Módulo de CARGA (LOAD)
Salva arquivos CSV em pastas padronizadas.
"""

import os
import pandas as pd

# Você pode mudar esse diretório ao subir para GitHub
DIRETORIO_RESULTADOS = "data/processed"
os.makedirs(DIRETORIO_RESULTADOS, exist_ok=True)


def salvar_csv(df: pd.DataFrame, nome_arquivo: str) -> None:
    """
    Salva DataFrame como CSV.
    """
    if df is None:
        print(f"⚠ Não há dados para salvar: {nome_arquivo}")
        return

    caminho = os.path.join(DIRETORIO_RESULTADOS, nome_arquivo)
    df.to_csv(caminho, index=False)
    print(f"📁 Arquivo salvo: {caminho}")
