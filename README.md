# MonteCarloSupplyChainExperiences

Este repositório apresenta uma aplicação simples em Flask para demonstração de experimentos de Monte Carlo em Supply Chain. A aplicação permite carregar um arquivo CSV com uma coluna `demand` e gera uma previsão por média móvel, além de cálculos de estoque de segurança e ponto de reposição.

## Estrutura do Projeto

```text
.
├── Dockerfile
├── requirements.txt
├── app.py
├── app
│   ├── __init__.py
│   ├── forecast.py
│   ├── inventory.py
│   └── routes.py
├── templates
│   ├── results.html
│   └── upload.html
├── ScriptComExperimentos.qmd
├── ScriptComExperimentos.html
└── Safety-Stock-Monte-Carlo-vf.xlsx
```

## Executando com Docker

1. Construa a imagem:

```bash
docker build -t montecarlo-app .
```

2. Rode o contêiner expondo a porta da aplicação:

```bash
docker run -p 5000:5000 montecarlo-app
```

A interface web ficará disponível em `http://localhost:5000`. Carregue seu CSV para visualizar a previsão e os parâmetros de inventário calculados.
