import streamlit as st

st.markdown("# Carrinho")
st.sidebar.markdown("# Carrinho")

st.title("🛒Carrinho")

if "carrinho" in st.session_state and len(st.session_state["carrinho"]) > 0:
    qtd_carrinho = {}

    for itens in st.session_state["carrinho"]:
        id_product = itens["id"]

        if id_product in qtd_carrinho:
            qtd_carrinho[id_product]["quantidade"] += 1
        else:
            qtd_carrinho[id_product] = {"nome": itens["nome"], "foto": itens["foto"], "quantidade": 1}