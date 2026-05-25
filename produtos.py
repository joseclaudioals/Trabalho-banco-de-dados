import psycopg2 as pg
import streamlit as st

st.markdown("# Produtos")
st.sidebar.markdown("# Produtos")

st.title("Aba dos Produtos")

conexao = pg.connect(
    host="localhost",
    database="trabalho bd",
    user="postgres",
    password="arthur25",
    port="5432"
)

cursor = conexao.cursor()

product_name = st.text_input('Busca de Produtos')

if product_name:
    cursor.execute("SELECT foto, nome, qnt FROM produto WHERE nome ILIKE %s", (f"%{product_name}%",))

    resultados = cursor.fetchall()

    for linha in resultados:
        v_foto = linha[0]
        v_nome = linha[1]
        v_qtd = linha[2]

        st.write("Foto: ", v_foto)
        st.write("Nome: ", v_nome)
        st.write("Quantidade: ", v_qtd)


st.write("Voce digitou: ", product_name)