import streamlit as st

main_page = st.Page("main.py", title="main page")
adm_page = st.Page("adm.py", title="adm page")
produtos_page = st.Page("produtos.py", title="produtos page")
carrinho_page = st.Page("carrinho.py", title="carrinho")

pg = st.navigation([main_page, adm_page, produtos_page, carrinho_page])

pg.run()