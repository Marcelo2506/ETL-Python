import streamlit as st
import pandas as pd
import plotly.express as px

# Titulo do Dashboard
st.title("Análise de KPIs de Anúncios")

# Upload do arquivo CSV
uploaded_file = st.file_uploader("Envie um arquivo CSV", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Tratando colunas
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df['Amount_spent'] = df['Amount_spent'].replace(
        {'R$': ''}, regex=True).astype(int)
    df['Link_clicks'] = pd.to_numeric(
        df['Link_clicks'], errors='coerce').fillna(0).astype(int)
    df['Conversion'] = pd.to_numeric(
        df['Conversion'], errors='coerce').fillna(0).astype(int)

    # Cálculo de KPIs
    kpi1 = df.groupby(df['Date'].dt.strftime('%Y-%m'))['Amount_spent'].sum()
    kpi2 = df.groupby(df['Date'].dt.strftime('%Y-%m'))['Conversion'].sum()
    kpi3 = df.groupby(df['Date'].dt.strftime('%Y-%m'))['Link_clicks'].sum()
    kpi4 = df.groupby(df['Date'].dt.strftime('%Y-%m'))['Amount_spent'].sum() / \
        df.groupby(df['Date'].dt.strftime('%Y-%m')
                   )['Conversion'].sum().fillna(0)

    # Exibição dos dados
    st.write("### Amostra dos Dados")
    st.dataframe(df.head())

    # Exibição dos KPIs
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Mês com Maior Gasto", value=str(kpi1.idxmax()))
    with col2:
        st.metric(label="Total de Conversões no Mês com Mais Gasto",
                  value=int(kpi2.max()))
    with col3:
        st.metric(label="Total de Cliques no Mês com Mais Gasto",
                  value=int(kpi3.max()))
    with col4:
        st.metric(label="Custo por Conversão Médio",
                  value=f"R$ {kpi4.mean():.2f}")

    # Gráfico de Gasto por Data
    st.write("### Gasto diário com Marketing")
    st.line_chart(df.groupby('Date')['Amount_spent'].sum())

    # Gráfico de Gasto por Segmentação
    st.write("### Gasto por Segmentação")
    segmentacao_gasto = df.groupby('Segmentação')[
        'Amount_spent'].sum().sort_values(ascending=False)
    st.bar_chart(segmentacao_gasto)

    # KPI Calculos
    df["CPC"] = (df["Amount_spent"]/df["Link_clicks"]
                 ).replace([float("inf"), float("nan")], 0)
    df["CPM"] = (df["Amount_spent"] / df["Impressions"] *
                 1000).replace([float("inf"), float("nan")], 0)
    df["CPA"] = (df["Amount_spent"] / df["Conversion"]
                 ).replace([float("inf"), float("nan")], 0)
    df["CTR (%)"] = (df["Amount_spent"] / df["Impressions"]
                     * 100).replace([float("inf"), float("nan")], 0)
    df["Conversion Rate (%)"] = (df["Conversion"] / df["Link_clicks"]
                                 * 100).replace([float("inf"), float("nan")], 0)

    # Análises Mensais Interativas
    st.subheader("Análise Mensal Interativa")
    df["Month"] = df["Date"].dt.month_name()
    months = df["Month"].unique().tolist()
    selected_month = st.selectbox("Selecione o Mês para Análise", months)

    column_options = ["Amount_spent",
                      "Link_clicks", "Impressions", "Conversion"]
    selected_column = st.selectbox(
        "Selecione o KPI para Análise", column_options)

    mes_df = df[df["Month"] == selected_month]
    daily_summary = (
        mes_df.groupby(df["Date"].dt.day)[selected_column].sum().reset_index()
    )
    daily_summary.columns = ["Day", selected_column]

    fig_mensal = px.bar(
        daily_summary,
        x="Dia",
        y=selected_column,
        title=f"Dia{selected_column} in {selected_month}",
        labels={"Day": "Dia do Mês", selected_month: selected_column}
    )

    st.plotly_chart(fig_mensal)

else:
    st.write("Por favor, Envie um Arquivo para Análise.")
