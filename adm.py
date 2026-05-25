import streamlit as st
import pandas as pd
import psycopg2 as pg

st.markdown("# administração")
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

if st.button("Ver o valor total de um pedido"):
    conexao = None

    try:

        conexao = pg.connect(
            host="localhost",
            database="ecommerce",
            user="postgres",
            password="jcals1009",
            port="5432"
        )

        cursor = conexao.cursor()

        query = "SELECT calcular_total_pedido(1)"
        cursor.execute(query)

        resultado = cursor.fetchall()
        nome_colunas = [desc[0] for desc in cursor.description]

        df = pd.DataFrame(resultado, columns = nome_colunas)

        st.success("Dados carregados com sucesso")
        st.dataframe(df, use_container_width=True)

        cursor.close()
    except Exception as e:
        st.error(e)
    finally:
        if conexao is not None:
            conexao.close()

st.sidebar.markdown("# Administrador")

