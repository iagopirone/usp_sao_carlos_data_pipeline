
# USP São Carlos – Pipeline Automatizado de Indicadores Institucionais
[🇺🇸 English](README_EN.md) | Português

![USP São Carlos](https://img.shields.io/badge/USP-São%20Carlos-0050A0)
![Projeto Institucional](https://img.shields.io/badge/Projeto-Institucional-blue)
![PUB-USP](https://img.shields.io/badge/PUB-USP%202024/2025-lightgrey)
![ETL](https://img.shields.io/badge/ETL-Produtivo-success)
![Validação](https://img.shields.io/badge/Validação-2019--2024-green)
![Reutilizável](https://img.shields.io/badge/Reutilizável-Anualmente-important)
![Licença](https://img.shields.io/badge/Licença-MIT-black)


Este repositório contém um pipeline completo para automação da coleta, filtragem e padronização dos principais indicadores do campus da USP São Carlos, extraídos diretamente do Anuário Estatístico da USP (USP Digital).

O projeto foi desenvolvido no âmbito do Programa Unificado de Bolsas (PUB-USP) com o objetivo de substituir o processo manual de obtenção de dados institucionais por uma solução reproduzível, padronizada e facilmente reutilizável em edições futuras do Anuário.

---

## Problema que o projeto resolve

O Anuário apresenta dados consolidados para toda a USP, o que obriga cada campus a realizar uma coleta manual para obter seus próprios indicadores.
Esse processo é lento, suscetível a erros, inconsistente entre anos e precisa ser refeito a cada nova edição.

Este pipeline elimina esse problema ao:

- realizar a extração direta das tabelas oficiais via HTTP;
- padronizar automaticamente colunas e formatos que variam entre edições;
- filtrar exclusivamente os dados referentes ao campus São Carlos;
- gerar arquivos finais prontos para análise em CSV;
- permitir a repetição anual do processo com esforço praticamente nulo.

---

## Avanço em relação ao cronograma oficial

De acordo com o cronograma previsto no edital do PUB-USP, o projeto está dividido em etapas distribuídas ao longo de 12 meses, incluindo estudo das tabelas, desenvolvimento gradual dos módulos, testes, documentação e treinamento.

A execução real iniciou-se em **04 de setembro**.  
Em menos de 3 meses trabalho, já foram concluídos:

- o módulo completo de extração;
- o módulo completo de transformação;
- o módulo de carga;
- o pipeline integrado, testado e validado com as edições de 2019 a 2024;
- a filtragem e padronização do campus São Carlos;
- a estrutura final de ETL (Extract, Transform, Load) em formato reutilizável.

O pipeline é totalmente genérico e independente do ano; as edições 2019–2024 foram utilizadas apenas para validação. O sistema está preparado para processar automaticamente quaisquer futuros Anuários, assim que forem publicados.

Conclusão: O motor de ETL está operacional 4 meses antes do previsto no cronograma oficial.

---

## Tech Stack
* **Linguagem:** Python
* **Manipulação de Dados:** Pandas (DataFrames, Pivot Tables, Cleaning)
* **Ingestão de Dados:** Requests (Web Scraping de arquivos estáticos)
* **Compatibilidade Excel:** OpenPyXL, xlrd

---
## Arquitetura do projeto

etl/
│── extract.py        # Download das tabelas diretamente do USP Digital
│── transform.py      # Padronização de colunas e filtragem de São Carlos
│── load.py           # Salvamento dos resultados em CSV
└── pipeline.py       # Orquestração completa do processo

data/
│── raw/              # (opcional) tabelas brutas, caso queira armazenar
└── processed/        # CSVs finais prontos para análise

notebooks/
└── usp_sao_carlos_data_pipeline.ipynb   # Notebook original usado no protótipo

docs/
└── PUB-Projeto.pdf   # Documento oficial com o cronograma e descrição do projeto

requirements.txt
README.md

## Sobre a pasta `data/raw`

A pasta `data/raw` representa o local reservado para armazenar arquivos brutos baixados do Anuário, antes de qualquer filtragem ou transformação.  
Ela faz parte da arquitetura padrão de projetos de engenharia de dados, especialmente quando há interesse em histórico, auditoria ou reprocessamento.

No entanto, como os arquivos brutos podem ser grandes e variam a cada edição do Anuário, a pasta permanece **vazia no GitHub**.  
Isso evita que o repositório se torne pesado e garante que apenas o código essencial permaneça versionado.

Localmente, o uso dessa pasta é opcional. Ela pode ser utilizada para:
- armazenar as tabelas originais (`.xls` ou `.csv`) baixadas do USP Digital;  
- manter histórico de dados para validação ou auditoria;  
- evitar downloads repetidos durante o desenvolvimento;  
- permitir reprocessamento offline.
