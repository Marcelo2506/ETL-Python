import pandas as pd
import streamlit as st
from Validador import Planilha
from pydantic import ValidationError


def validar_dados(df):
    erros = []
    dados_validados = []

    for index, row in df.iterrows():
        try:
            # Converte a linha do df para dicionário
            dados = row.to_dict()

            # Valida os dados usando Planilha
            planilha_validada = Planilha(**dados)
            dados_validados.append(planilha_validada)

        except ValidationError as e:
            erros.append(f"Erro na linha {index + 2}: {str(e)}")

    return dados_validados, erros


def main():
    st.title("Validador de Dados de Campanhas")
    st.write("Upload do arquivo CSV para validação")

    uploaded_file = st.file_uploader("Escolha um arquivo CSV", type="csv")

    if uploaded_file is not None:
        try:
            # lê o arquivo
            df = pd.read_csv(uploaded_file)

            st.write("Preview dos dados:")
            st.dataframe(df.head())

            if st.button("Validar Dados"):
                with st.spinner("Validando dados..."):
                    dados_validados, erros = validar_dados(df)

                    if erros:
                        st.error("Foram encontrados erros na validação:")
                        for erro in erros:
                            st.write(erro)
                    else:
                        st.success(
                            "Todos os dados foram validados com sucesso!")

                        # Exibe quantidade de registros validados
                        st.write(
                            f"Total de registros validados: {len(dados_validados)}")

                        # Download dos dados
                        df_validado = pd.DataFrame(
                            [dados.dict() for dados in dados_validados])
                        st.download_button(
                            label="Download dos dados validados",
                            data=df_validado.to_csv(index=False),
                            file_name="Dados_validados.csv",
                            mime="text/csv"
                        )

        except Exception as e:
            st.error(f"Erro ao processar o arquivo: {str(e)}")


if __name__ == "__main__":
    main()
