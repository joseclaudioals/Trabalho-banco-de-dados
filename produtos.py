import streamlit as st

if "carrinho" not in st.session_state:
    st.session_state["carrinho"] = []

st.markdown("# Produtos")
st.sidebar.markdown("# Produtos")

st.title("📦Aba dos Produtos")

conexao = st.connection("postgresql", type="sql")

product_name = st.text_input('Busca de Produtos')

if product_name:
    resultados = conexao.query("SELECT id_produto, foto, nome, qnt FROM produto WHERE nome ILIKE :busca", params={"busca": f"%{product_name}%"})

else:
    resultados = conexao.query("SELECT id_produto, foto, nome, qnt FROM produto")

colunas = st.columns(3)

for index, linha in resultados.iterrows():
    v_id = linha["id_produto"]
    v_foto = "imagens/3maiores.png"
    v_nome = linha["nome"]
    v_qtd = linha["qnt"]

    coluna_alvo = colunas[index % 3]

    with coluna_alvo:
        st.image(v_foto, width=200)
        layout_texto = f"""
        <div style="display: flex; justify-content: space-between; margin-bottom: 30px; margin-right: 25px;">
            <strong>{v_nome}</strong>
            <span>Qtd: {v_qtd}</span>
        </div>
    """
        st.markdown(layout_texto, unsafe_allow_html=True)
        if st.button("Adicionar Carrinho", key=v_nome):
            st.session_state["carrinho"].append({"id": v_id, "nome": v_nome, "foto": v_foto})
            st.success(f"{v_nome} adicionado ao carrinho!")

st.write(st.session_state["carrinho"])