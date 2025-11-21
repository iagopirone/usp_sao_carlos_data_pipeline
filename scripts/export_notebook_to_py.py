"""
Script utilitário para converter notebooks (.ipynb) em arquivos .py padronizados.

Uso:
    python export_notebook_to_py.py caminho/do/notebook.ipynb saida.py

Exemplo:
    python export_notebook_to_py.py ../notebooks/usp_sao_carlos_data_pipeline.ipynb ../etl/codigo_extraido.py
"""

import json
import sys
from pathlib import Path


def extrair_codigo_do_notebook(caminho_notebook: Path):
    """Extrai todas as células de código de um arquivo .ipynb."""
    with open(caminho_notebook, "r", encoding="utf-8") as f:
        notebook = json.load(f)

    codigo = []
    for cell in notebook.get("cells", []):
        if cell.get("cell_type") == "code":
            fonte = "".join(cell.get("source", []))
            codigo.append(f"# ==== Célula de código ====\n{fonte}\n")

    return "\n".join(codigo)


def salvar_arquivo(destino: Path, conteudo: str):
    """Salva o conteúdo extraído em um arquivo .py."""
    destino.parent.mkdir(parents=True, exist_ok=True)

    with open(destino, "w", encoding="utf-8") as f:
        f.write(conteudo)

    print(f"Arquivo gerado com sucesso: {destino.absolute()}")


def main():
    if len(sys.argv) != 3:
        print("Uso correto:")
        print("python export_notebook_to_py.py caminho/do/notebook.ipynb saida.py")
        sys.exit(1)

    caminho_notebook = Path(sys.argv[1])
    caminho_saida = Path(sys.argv[2])

    if not caminho_notebook.exists():
        print(f"Erro: arquivo '{caminho_notebook}' não encontrado.")
        sys.exit(1)

    print(f"Lendo notebook: {caminho_notebook}")
    conteudo = extrair_codigo_do_notebook(caminho_notebook)

    print("Gerando arquivo .py...")
    salvar_arquivo(caminho_saida, conteudo)


if __name__ == "__main__":
    main()
