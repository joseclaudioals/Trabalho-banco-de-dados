import streamlit as st
import datetime
import importlib
from sqlalchemy import text

st.set_page_config(page_title="Loja de Lingerie", page_icon="👙")

conexao = st.connection("postgresql", type="sql")

if 'usuario_logado' not in st.session_state:
    st.session_state['usuario_logado'] = None
if 'tipo_usuario' not in st.session_state:
    st.session_state['tipo_usuario'] = None

if st.session_state['usuario_logado'] is None:
    st.title("👙 Bem-vindo à Loja de Lingerie 👙")

    aba_login, aba_cadastro = st.tabs(["Login", "Cadastrar Cliente"])

    with aba_login:
        st.subheader("Entrar no Sistema")
        email_login = st.text_input("E-mail")
        senha_login = st.text_input("Senha", type="password")

        if st.button("Entrar"):
            if email_login == "admin@loja.com" and senha_login == "1234":
                st.session_state['usuario_logado'] = "Administrador Geral"
                st.session_state['tipo_usuario'] = 'Admin'
                st.rerun()
            else:
                with conexao.session as session:
                    sql_login = text("SELECT nome_cliente FROM cliente WHERE email = :email AND senha = :senha")
                    resultado = session.execute(sql_login, {"email": email_login, "senha": senha_login}).fetchone()

                if resultado:
                    st.session_state['usuario_logado'] = resultado[0]
                    st.session_state['tipo_usuario'] = 'Cliente'
                    st.rerun()
                else:
                    st.error("Email ou senha incorretos!")

    with aba_cadastro:
        st.subheader("Novo Cliente")

        with st.form("form_cadastro_cliente"):
            nome_cad = st.text_input("Nome Completo")
            email_cad = st.text_input("E-mail")
            senha_cad = st.text_input("Senha", type="password")
            nasc_cad = st.date_input("Data de Nascimento", min_value=datetime.date(1900, 1, 1), max_value=datetime.date.today(), format="DD/MM/YYYY")
            telefone_cad = st.text_input("Telefone (Apenas números, 11 dígitos)")
            cep_cad = st.text_input("CEP (Apenas números, 8 dígitos)")
            num_cad = st.text_input("Número da Casa")

            submit_cadastro = st.form_submit_button("Cadastrar")

            if submit_cadastro:
                try:
                    with conexao.session as session:
                        sql_cadastro = text("""
                            INSERT INTO cliente (email, senha, nome_cliente, data_nascimento, telefone, cep, numero_casa)
                            VALUES (:email, :senha, :nome, :nasc, :tel, :cep, :num)
                        """)
                        session.execute(sql_cadastro, {
                            "email": email_cad,
                            "senha": senha_cad,
                            "nome": nome_cad,
                            "nasc": nasc_cad,
                            "tel": telefone_cad,
                            "cep": cep_cad,
                            "num": num_cad
                        })
                        session.commit()
                    st.success("Cadastro realizado com sucesso! Vá para a aba Login.")
                except Exception as e:
                    st.error(f"Erro ao salvar no banco: {e}")
else:
    st.sidebar.title(f"Olá, {st.session_state['usuario_logado']} 👋")
    if st.sidebar.button("Sair / Logout"):
        st.session_state['usuario_logado'] = None
        st.session_state['tipo_usuario'] = None
        st.rerun()

    if st.session_state['tipo_usuario'] == 'Cliente':
        opcoes_menu = ["Produtos", "Carrinho"]
    else:
        opcoes_menu = ["Produtos", "Carrinho", "Administração"]
        
    pagina = st.sidebar.selectbox("Menu de Navegação", opcoes_menu)
    
    if pagina == "Produtos":
        import produtos
        importlib.reload(produtos)
    elif pagina == "Carrinho":
        import carrinho
        importlib.reload(carrinho)
    elif pagina == "Administração":
        import adm
        importlib.reload(adm)

#streamlit run main.py