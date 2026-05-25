import streamlit as st
import pandas as pd
import psycopg2 as pg


tab1, tab2, tab3 = st.tabs(["Editar produtos", "Funções basicas","Logs de administrador"])

with tab1:
    st.header("# Editar produtos")
with tab2:
    st.header("Funções basicas")
    if st.button("Ver o valor total de um pedido"):
        conn = st.connection("postgre", type = "sql")
        df = conn.query("SELECT * FROM produto", ttl = 660)
        st.dataframe(df)
with tab3:
    st.header("logs de administrador")
