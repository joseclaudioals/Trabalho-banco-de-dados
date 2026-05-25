import streamlit as st
import pandas as pd
from sqlalchemy import text

conn = st.connection("postgresql", type="sql")

tab1, tab2, tab3 = st.tabs(["Editar produtos", "Funções basicas","Logs de administrador"])

with tab1:
    st.header("Editar produtos")

    with st.form(key="editar_produtos"):
        #id produto
        id = st.number_input("Id do produto", value=0, step=1)
        # nome
        nome = st.text_input("Nome do produto")
        # descricao
        descricao = st.text_input("Decrição do produto")
        # cor
        cor = st.text_input("Cor do produto")
        # tamanho
        tamanho = st.selectbox("Tamanho do produto", ("pp", "p", "m", "g", "gg"))
        # preco unitario
        preco = st.number_input("Preco do produto")

        bt_editar = st.form_submit_button("editar")
    if bt_editar:
        sql = text('''
            UPDATE produto SET 
                nome = :nome, 
                descricao = :descricao,
                cor = :cor,
                tamanho = :tamanho,
                preco_unitario = :preco
            WHERE id_produto = :id;
        ''')

        parametros = {
            "nome": nome,
            "descricao": descricao,
            "cor": cor,
            "tamanho": tamanho,
            "preco": preco,
            "id": id
        }

        with conn.session as session:
            resultado = session.execute(sql, parametros)

            if resultado.rowcount == 0:
                st.warning(f"Alerta: o ID {id} nao foi encontrado, nenhuma alteração feita")
            else:
                log = text('''
                    INSERT INTO auditoria (id_funcionario, id_produto, descricao_auditoria, data_auditoria)
                    VALUES (1, :id_produto, 'Alteração nas propriedades de um produto', NOW());
                ''')
                session.execute(log, {"id_produto": id})

                session.commit()

                st.success("Alteração realizada com sucesso")
                st.cache_data.clear()

with tab2:
    st.header("Funções basicas")

    with st.form(key="estoque_critico"):
        st.markdown("### Verificar estoque critico:")
        n = st.number_input("quantidade de items", value=0, step=1)

        bt = st.form_submit_button("buscar")

    if bt:
        sql = '''
                SELECT verificar_estoque_critico(:n);
            '''
        df = conn.query(sql, params={"n": n}, ttl=660)
        st.dataframe(df)

    with st.form(key="obter_categoria"):
        st.markdown("### Obter categoria do cliente:")
        n = st.number_input("id do cliente", value=0, step=1)

        bt_categoria = st.form_submit_button("buscar")

    if bt_categoria:
        sql = '''
                SELECT obter_categoria_cliente(:n);
            '''
        df = conn.query(sql, params={"n": n}, ttl=660)
        st.dataframe(df)


    if st.button("Ver todos os produtos"):
        sql = '''
            SELECT * FROM produto;
        '''
        df = conn.query(sql, ttl=660)
        st.dataframe(df)

    st.markdown("## Views")

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Ver cargo dos funcionarios"):
            sql = '''
                SELECT * FROM funcionario_cargo;
            '''
            df = conn.query(sql, ttl=660)
            st.dataframe(df)

    with col2:
        if st.button("Ver produtos gg"):
            sql = '''
                SELECT * FROM tamanho_produto;
            '''
            df = conn.query(sql, ttl=660)
            st.dataframe(df)

    with col3:
        if st.button("Ver fechamento financeiro"):
            sql = '''
                SELECT * FROM fechamento_financeiro;
            '''
            df = conn.query(sql, ttl=660)
            st.dataframe(df)

with tab3:
    st.header("logs de administrador")

    if st.button("Ver logs de administrador"):

        sql = '''
            SELECT f.nome_funcionario as Funcionario_responsavel, 
                   p.nome as Produto_modificado, 
                   a.descricao_auditoria
            FROM funcionario f
            JOIN auditoria a
            ON f.id_funcionario = a.id_funcionario
            JOIN produto p
            ON p.id_produto = a.id_produto
        '''

        df = conn.query(sql, ttl=120)
        st.dataframe(df)