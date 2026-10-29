# ✅ Hábitos Diários — Dashboard

Meu primeiro app em Python: um dashboard que transforma o registro diário de hábitos e estudos em indicadores e gráficos, para eu ver onde preciso melhorar e onde já me dedico o suficiente.

**🔗 Demo:** https://habitos-diarios-python-hcscc84edqtme626etl9ew.streamlit.app/

![Dashboard](docs/dashboard.jpg)

## Como surgiu

O projeto nasceu em 3 etapas:

1. **Código em Python** para registrar os hábitos (`habitos-diarios.py`).
2. **Gravação dos dados em CSV**, para guardar o histórico.
3. **Dashboard em Streamlit** (`app.py`), que lê o CSV, trata os dados com pandas e mostra os resultados.

Eu defini as métricas, organizei o repositório e fiz o deploy. Na publicação, corrigi um bug que deixava o app em branco, causado por configuração errada (branch e arquivo principal).

## O que ele mostra

- Taxa de conclusão, dias registrados, sequência atual e melhor sequência
- Hábito mais consistente e hábito que precisa de atenção
- Evolução diária com média móvel de 7 dias e linha de meta
- Conclusão por hábito
- Desempenho por dia da semana
- Calendário de hábitos (um quadrado por hábito e dia)
- Filtros de período e de hábitos, e meta diária ajustável

## Como rodar

```bash
git clone https://github.com/V2024/habitos-diarios-python.git
cd habitos-diarios-python
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

## Estrutura

```
├── app.py                  # dashboard (Streamlit)
├── habitos-diarios.py      # script que registra os hábitos em CSV
├── dados/                  # CSV de exemplo
├── docs/                   # print do dashboard
├── .streamlit/config.toml  # tema visual
└── requirements.txt
```

## Tecnologias

Python · pandas · Streamlit · Altair

## Próximos passos (versão 2)

- Guardar os registros em SQLite em vez de CSV
- Adicionar mais funcionalidades ao dashboard
- Gerar um resumo semanal dos hábitos com IA
