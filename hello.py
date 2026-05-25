import streamlit as st

import psycopg2 as pg

try:
    conexao = pg.connect(
        host="localhost",
        database = "ecommerce",
        user="postgres",
        password="1234",
        port="5432"
    )

    print("conexao ok")

    cursor = conexao.cursor()

    cursor.execute("SELECT VERSION()")
    resultado = cursor.fetchone()
    print(resultado[0])

    cursor.close()
except Exception as erro:
    print("erro ao conectar")
finally:
    if 'conexao' in locals() and conexao is not None:
        conexao.close()
        print("conexao fechada")