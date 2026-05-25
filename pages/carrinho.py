import streamlit as st
from sqlalchemy import text

st.markdown("# Carrinho")
st.sidebar.markdown("# Carrinho")
st.title("🛒 Meu Carrinho (Modo Relacional)")

conexao = st.connection("postgresql", type="sql")

ID_CARRINHO_TESTE = 1

query_carrinho = """
    SELECT 
        p.id_produto, 
        p.nome, 
        p.foto, 
        p.preco_unitario, 
        cp.qtd_produto_carrinho
    FROM carrinho_produto cp
    INNER JOIN produto p ON cp.id_produto = p.id_produto
    WHERE cp.id_carrinho = :id_carrinho;
"""

resultados = conexao.query(query_carrinho, params={"id_carrinho": ID_CARRINHO_TESTE})

if not resultados.empty:

    total_geral = 0.0
    st.markdown("---")

    for index, linha in resultados.iterrows():
        v_id_produto = linha["id_produto"]
        v_nome = linha["nome"]
        v_foto = "imagens/3maiores.png"  # Ou linha["foto"] se as imagens mudarem
        v_preco = linha["preco_unitario"]
        v_quantidade = linha["qtd_produto_carrinho"]

        subtotal = v_preco * v_quantidade
        total_geral += subtotal

        # Desenhamos o grid na tela
        col_foto, col_nome, col_qtd, col_sub = st.columns([1, 3, 1, 1])

        with col_foto:
            st.image(v_foto)

        with col_nome:
            st.write(f"**{v_nome}**")

        with col_qtd:
            st.write(f"Quantidade: {v_quantidade}")

        with col_sub:
            st.write(f"Subtotal: R$ {subtotal}")

    st.markdown("---")
    st.markdown(f"### 💵 Total do Pedido: R$ {total_geral}")

    if st.button("Finalizar a Compra"):
        with conexao.session as s:

            sql_pedido = text("""
                INSERT INTO pedido (id_cliente, frete) 
                VALUES (:cliente, :frete) 
                RETURNING id_pedido;
            """)
            id_pedido_gerado = s.execute(sql_pedido, params={"cliente": 1, "frete": 0.0}).fetchone()[0]

            for index, linha in resultados.iterrows():
                sql_item = text("""
                    INSERT INTO produto_pedido (id_pedido, id_produto, quantidade_compra, preco_unitario) 
                    VALUES (:pedido, :produto, :qtd, :preco);
                """)
                s.execute(sql_item, params={
                    "pedido": id_pedido_gerado,
                    "produto": linha["id_produto"],
                    "qtd": linha["qtd_produto_carrinho"],
                    "preco": linha["preco_unitario"]
                })

            sql_limpar_carrinho = text("DELETE FROM carrinho_produto WHERE id_carrinho = :id_carrinho;")
            s.execute(sql_limpar_carrinho, params={"id_carrinho": ID_CARRINHO_TESTE})

            s.commit()

        st.success(f"Compra gravada com sucesso! Pedido gerado: No {id_pedido_gerado}")
        st.rerun()
else:
    st.warning("O seu carrinho está vazio no banco de dados no momento.")