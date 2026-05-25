import streamlit as st
import psycopg2
import datetime
import importlib

def conectar_banco():
    return psycopg2.connect(
        host="localhost",
        database="ecommerce",
        user="postgres",
        password="1234",
        port="5432"
    )

st.set_page_config(page_title="Loja de Lingerie", page_icon="👙")

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
                conn = conectar_banco()
                cur = conn.cursor()

                cur.execute("SELECT nome_cliente FROM cliente WHERE email = %s AND senha = %s", (email_login, senha_login))
                resultado = cur.fetchone()

                if resultado:
                    st.session_state['usuario_logado'] = resultado[0]
                    st.session_state['tipo_usuario'] = 'Cliente'
                    st.rerun()
                else:
                    st.error("Email ou senha incorretos!")
                
                cur.close()
                conn.close()

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
                    conn = conectar_banco()
                    cur = conn.cursor()
                    cur.execute("""
                        INSERT INTO cliente (email, senha, nome_cliente, data_nascimento, telefone, cep, numero_casa)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """, (email_cad, senha_cad, nome_cad, nasc_cad, telefone_cad, cep_cad, num_cad))
                    conn.commit()
                    st.success("Cadastro realizado com sucesso! Vá para a aba Login.")
                except Exception as e:
                    conn.rollback()
                    st.error(f"Erro ao salvar no banco: {e}")
                finally:
                    cur.close()
                    conn.close()

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