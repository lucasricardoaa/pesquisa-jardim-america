# Análise de Dados — Pesquisa Extensionista Jardim América

Script em Python desenvolvido para a **Atividade Extensionista II: Tecnologia Aplicada à Inclusão Digital — Projeto**, do curso de **CST em Ciência de Dados** (UNINTER).

O projeto teve como objetivo coletar e analisar a opinião de moradores do bairro Jardim América (Rio de Janeiro, RJ) sobre as condições de infraestrutura e serviços locais, identificando oportunidades de melhoria para a comunidade.

## Contexto do projeto

- **Coleta de dados:** questionário aplicado via Google Forms, divulgado por WhatsApp
- **Período de coleta:** 02 a 04 de junho de 2026
- **Total de respondentes:** 20 moradores
- **Organização dos dados:** Google Sheets
- **Análise dos dados:** Python (este repositório)

## Bibliotecas utilizadas

- [`pandas`](https://pandas.pydata.org/) — manipulação e tratamento dos dados
- [`matplotlib`](https://matplotlib.org/) — geração dos gráficos
- [`numpy`](https://numpy.org/) — cálculos auxiliares

## O que o script faz

1. Calcula a média de avaliação (escala 1 a 5) para cada aspecto do bairro avaliado: iluminação pública, limpeza, ruas e calçadas, transporte, segurança, saúde, educação e comércio
2. Gera gráfico de barras com as médias por aspecto, destacando os itens críticos
3. Gera gráfico de distribuição dos respondentes por faixa etária
4. Gera gráfico de pizza com o tempo de moradia dos respondentes no bairro
5. Gera gráfico de distribuição das notas do aspecto mais crítico identificado (segurança)
6. Exibe um resumo textual da análise no terminal, incluindo médias, aspecto mais bem avaliado, aspecto mais crítico e principais problemas mencionados nas respostas abertas

## Como reproduzir a análise

> **Nota sobre privacidade:** o arquivo CSV com as respostas individuais dos moradores não está incluído neste repositório, por conter dados pessoais (nomes informados voluntariamente). Para reproduzir a análise, utilize seus próprios dados exportados do Google Forms.

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/pesquisa-jardim-america.git
cd pesquisa-jardim-america

# Instale as dependências
pip install -r requirements.txt

# Coloque o CSV exportado do Google Forms na mesma pasta, renomeado para "respostas.csv"

# Execute o script
python analise.py
```

Os gráficos gerados serão salvos na pasta `outputs/`.

## Principais resultados obtidos

A segurança pública foi identificada como o aspecto mais crítico do bairro, com média de 1,50 em uma escala de 1 a 5 — a mais baixa entre todos os itens avaliados. Esse resultado foi reforçado pelas respostas abertas: 9 dos 20 respondentes apontaram a segurança como o maior problema do bairro atualmente.

Os aspectos mais bem avaliados foram comércio e serviços básicos (3,45) e limpeza e coleta de lixo (3,40).

## Autor

Lucas Ricardo Avelino de Araújo
CST em Ciência de Dados — UNINTER
