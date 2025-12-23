# 📊 ETL Project

## 🧠 Sobre o Projeto

Este projeto implementa um pipeline **ETL (Extract, Transform, Load)** em Python para demonstrar o processo completo de extração, transformação e carregamento de dados — conceitos fundamentais em **Engenharia de Dados e Analytics**.  
O objetivo é automatizar a coleta de dados, realizar transformações de limpeza e formatação, e armazenar os dados processados para uso posterior em análises ou dashboards.

O processo ETL é um padrão amplamente utilizado em projetos de dados para consolidar informações de diferentes fontes e preparar dados prontos para análise ou armazenamento em banco de dados ou estrutura de dados final.:contentReference[oaicite:0]{index=0}

---

## 🚀 Funcionalidades

O ETL deste projeto realiza as seguintes etapas:

1. **Extração**  
   - Leitura de dados de uma ou mais fontes (ex: arquivos CSV, API ou bancos de dados)

2. **Transformação**  
   - Limpeza e transformação dos dados com o objetivo de padronizar, tratar valores faltantes e gerar novos campos relevantes

3. **Carga (Load)**  
   - Armazenamento dos dados transformados em destino final (por exemplo, CSV limpo, banco de dados ou outro formato)

---

## 🗂 Estrutura do Projeto

```text
ETL-project/
├── extract.py          # Lógica de extração de dados
├── transform.py        # Regras de limpeza e transformação
├── load.py             # Funções de carregamento para destino
├── pipeline.py         # Script principal que executa o fluxo ETL
├── requirements.txt    # Dependências do projeto
├── data/               # Arquivos de dados de entrada e saída
│   ├── raw/
│   └── processed/
├── notebooks/          # Notebooks para exploração e testes
└── README.md
