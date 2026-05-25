import streamlit as st
import pandas as pd
import psycopg2 as pg

conn = st.connection("postgre", type="sql")
tab1, tab2, tab3 = st.tabs(["Editar produtos", "Funções basicas","Logs de administrador"])

with tab1:
    st.header("# Editar produtos")
with tab2:
    st.header("Funções basicas")

    with st.form(key="estoque_critico"):
        st.markdown("# Verificar estoque critico:")
        n = st.number_input("quantidade de items a serem visualidada", value=0, step=1)

        bt = st.form_submit_button("buscar")

    if bt:
        sql = '''
                SELECT verificar_estoque_critico(:n);
            '''
        df = conn.query(sql, params={"n": n}, ttl=660)
        st.dataframe(df)

    if st.button("Ver todos os produtos"):


        sql = '''
            SELECT * FROM produto;
        '''
        df = conn.query(sql,ttl = 660)
        st.dataframe(df)
with tab3:
    st.header("logs de administrador")
