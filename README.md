# ✅ Hábitos Diários — Dashboard

Dashboard em Python (Streamlit + pandas) que transforma o registro diário de hábitos em indicadores e gráficos: taxa de conclusão, sequências de dias, evolução com média móvel e melhores dias da semana.

**Demo:** _cole aqui o link do Streamlit Cloud_

![Dashboard](docs/dashboard.png)

## O que ele mostra

- Taxa de conclusão, dias registrados, sequência atual e melhor sequência
- Evolução diária com média móvel de 7 dias
- Conclusão por hábito
- Desempenho por dia da semana
- Filtros de período e de hábitos, e meta diária ajustável

## Como rodar

```bash
git clone https://github.com/V2024/habitos-diarios.git
cd habitos-diarios
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

Sem dados reais, o app abre com `dados/habitos_exemplo.csv`.

## Formato do CSV

Coloque seu arquivo em `dados/habitos.csv`:

| coluna | exemplo | observação |
|--------|---------|------------|
| data   | 2026-10-27 ou 27/10/2026 | uma linha por hábito por dia |
| habito | Estudar Python | nome do hábito |
| feito  | 1 / 0, sim / não | concluído ou não |

Se os nomes das colunas forem outros, ajuste as constantes `COL_DATA`, `COL_HABITO` e `COL_FEITO` no topo do `app.py`.

## Tecnologias

Python · pandas · Streamlit

## Deploy

Publicado no Streamlit Community Cloud apontando para `app.py`.

## Próximos passos

- Integrar com IA para gerar um resumo semanal dos hábitos
- Salvar os registros em SQLite
