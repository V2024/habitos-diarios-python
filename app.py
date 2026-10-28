"""Dashboard do projeto Hábitos Diários.

Como rodar:
    pip install streamlit pandas numpy
    streamlit run app.py

O CSV esperado fica em dados/habitos.csv, com as colunas:
    data    -> 2026-10-27 ou 27/10/2026
    habito  -> nome do hábito (ex.: Estudar Python)
    feito   -> 1/0, sim/não ou true/false

Se os nomes das colunas do seu CSV forem diferentes, ajuste só as três
constantes abaixo. Sem o CSV real, o app usa dados/habitos_exemplo.csv.
"""
from pathlib import Path

import numpy as np
import pandas as pd
import streamlit as st

CSV = Path("dados/habitos.csv")
CSV_EXEMPLO = Path("dados/habitos_exemplo.csv")
COL_DATA = "data"
COL_HABITO = "habito"
COL_FEITO = "feito"

VERDADEIRO = {"1", "sim", "s", "true", "feito", "x", "ok", "yes"}
DIAS = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"]

st.set_page_config(page_title="Hábitos Diários", page_icon="✅", layout="wide")


def dados_demo():
    rng = np.random.default_rng(42)
    datas = pd.date_range(end=pd.Timestamp.today().normalize(), periods=60)
    habitos = ["Estudar Python", "Exercício", "Leitura", "Beber água"]
    probs = [0.75, 0.55, 0.65, 0.85]
    linhas = [
        {COL_DATA: d, COL_HABITO: h, COL_FEITO: int(rng.random() < p)}
        for d in datas
        for h, p in zip(habitos, probs)
    ]
    return pd.DataFrame(linhas)


@st.cache_data
def carregar():
    demo = not CSV.exists()
    if not demo:
        df = pd.read_csv(CSV)
    elif CSV_EXEMPLO.exists():
        df = pd.read_csv(CSV_EXEMPLO)
    else:
        df = dados_demo()
    df[COL_DATA] = pd.to_datetime(df[COL_DATA], dayfirst=True, errors="coerce")
    df = df.dropna(subset=[COL_DATA])
    df["feito"] = (
        df[COL_FEITO].astype(str).str.strip().str.lower().isin(VERDADEIRO).astype(int)
    )
    df["habito"] = df[COL_HABITO].astype(str).str.strip()
    df["data"] = df[COL_DATA].dt.normalize()
    return df[["data", "habito", "feito"]], demo


def sequencias(bateu):
    atual = melhor = 0
    for ok in bateu:
        atual = atual + 1 if ok else 0
        melhor = max(melhor, atual)
    return atual, melhor


df, demo = carregar()

st.title("✅ Hábitos Diários")
if demo:
    st.info("Mostrando dados de exemplo. Coloque seu CSV em dados/habitos.csv.")

# ---------- Filtros ----------
with st.sidebar:
    st.header("Filtros")
    inicio, fim = st.date_input(
        "Período",
        value=(df["data"].min().date(), df["data"].max().date()),
        min_value=df["data"].min().date(),
        max_value=df["data"].max().date(),
    )
    escolhidos = st.multiselect(
        "Hábitos", sorted(df["habito"].unique()), default=sorted(df["habito"].unique())
    )
    meta = st.slider("Meta diária (%)", 10, 100, 70, step=10)

filtrado = df[
    (df["data"].dt.date >= inicio)
    & (df["data"].dt.date <= fim)
    & (df["habito"].isin(escolhidos))
]

if filtrado.empty:
    st.warning("Nenhum registro com esses filtros.")
    st.stop()

# ---------- Cálculos ----------
diario = filtrado.groupby("data")["feito"].mean() * 100
calendario = pd.date_range(diario.index.min(), diario.index.max())
diario = diario.reindex(calendario)
bateu = (diario >= meta).fillna(False)
atual, melhor = sequencias(bateu)

# ---------- Indicadores ----------
c1, c2, c3, c4 = st.columns(4)
c1.metric("Taxa de conclusão", f"{filtrado['feito'].mean() * 100:.0f}%")
c2.metric("Dias registrados", int(diario.notna().sum()))
c3.metric("Sequência atual", f"{atual} dias")
c4.metric("Melhor sequência", f"{melhor} dias")

# ---------- Gráficos ----------
st.subheader("Evolução diária")
evolucao = pd.DataFrame(
    {"Diário (%)": diario, "Média 7 dias (%)": diario.rolling(7, min_periods=1).mean()}
)
st.line_chart(evolucao)

col_a, col_b = st.columns(2)

with col_a:
    st.subheader("Conclusão por hábito")
    por_habito = (filtrado.groupby("habito")["feito"].mean() * 100).sort_values()
    st.bar_chart(por_habito, horizontal=True)

with col_b:
    st.subheader("Melhores dias da semana")
    por_dia = filtrado.assign(dia=filtrado["data"].dt.dayofweek)
    por_dia = (por_dia.groupby("dia")["feito"].mean() * 100).reindex(range(7))
    por_dia.index = DIAS
    st.bar_chart(por_dia)

with st.expander("Ver registros"):
    st.dataframe(filtrado.sort_values("data", ascending=False))
