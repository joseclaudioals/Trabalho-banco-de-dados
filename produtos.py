import streamlit as st
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

st.markdown("# Produtos")
st.sidebar.markdown("# Produtos")
st.title("📦 Aba dos Produtos")

conexao = st.connection("postgresql", type="sql")
product_name = st.text_input('Busca de Produtos')

if product_name:
    resultados = conexao.query(
        "SELECT id_produto, foto, nome, qnt, preco_unitario FROM produto WHERE nome ILIKE :busca",
        params={"busca": f"%{product_name}%"})
else:
    resultados = conexao.query("SELECT id_produto, foto, nome, qnt, preco_unitario FROM produto")

colunas = st.columns(3)

for index, linha in resultados.iterrows():
    v_id = linha["id_produto"]
    v_foto = "imagens/3maiores.png"
    v_nome = linha["nome"]
    v_qtd = linha["qnt"]
    v_preco = linha["preco_unitario"]

    coluna_alvo = colunas[index % 3]

    with coluna_alvo:
        st.image(v_foto, width=200)
        layout_texto = f"""
        <div style="display: flex; justify-content: space-between; margin-bottom: 30px; margin-right: 25px;">
            <strong>{v_nome}</strong>
            <span>Estoque: {v_qtd}</span>
        </div>
        """
        st.markdown(layout_texto, unsafe_allow_html=True)

        if st.button("Adicionar Carrinho", key=f"btn_{v_id}"):

            try:
                id_cliente = st.session_state.get("id_cliente", 1)

                with conexao.session as s:

                    if "meu_carrinho_id" not in st.session_state:
                        sql_criar = text("INSERT INTO carrinho (id_cliente, data_criacao) VALUES (:id_cliente, CURRENT_TIMESTAMP) RETURNING id_carrinho;")
                        id_gerado = s.execute(sql_criar, {"id_cliente": id_cliente}).fetchone()[0]
                        s.commit()
                        st.session_state["meu_carrinho_id"] = id_gerado

                    carrinho_dinamico = st.session_state["meu_carrinho_id"]

                    sql_upsert = text("""
                        INSERT INTO carrinho_produto (id_carrinho, id_produto, qtd_produto_carrinho) 
                        VALUES (:carrinho, :produto, 1)
                        ON CONFLICT (id_carrinho, id_produto) 
                        DO UPDATE SET qtd_produto_carrinho = carrinho_produto.qtd_produto_carrinho + 1;
                    """)
                    s.execute(sql_upsert, params={"carrinho": carrinho_dinamico, "produto": v_id})
                    s.commit()

                st.success(f"{v_nome} adicionado ao carrinho!")

            except SQLAlchemyError as e:
                st.error(f"⚠️ O PostgreSQL barrou por este motivo: {e}")