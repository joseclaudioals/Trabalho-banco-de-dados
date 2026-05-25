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
            qtd_carrinho[id_product] = {"nome": itens["nome"], "foto": itens["foto"], "preco": itens["preco"], "quantidade": 1}

    st.markdown("---")

    total_geral = 0.0
    for id_product, dados in qtd_carrinho.items():
        subtotal = dados["preco"] * dados["quantidade"]

        total_geral += subtotal

        col_foto, col_nome, col_qtd, col_sub = st.columns([1, 3, 1, 1])

        with col_foto:
            st.image(dados["foto"])

        with col_nome:
            st.write(f"**{dados['nome']}**")

        with col_qtd:
            st.write(f"Quantidade: {dados['quantidade']}")

        with col_sub:
            st.write(f"Subtotal: R${subtotal}")

    st.markdown("---")

    st.markdown(f"💵Total do Pedido: R$ {total_geral}")

    if st.button("Finalizar a Compra"):
        st.success("Preparando o INSERT do banco de dados")

else:
    st.warning("O seu carrinho está vazio no momento.")