import sqlite3

def conectar():
    return sqlite3.connect("cadastros.db")

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cadastros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            email TEXT,
            telefone TEXT,
            cpf TEXT,
            data_nascimento TEXT
        )
    """)
    conn.commit()
    conn.close()

def salvar_dados(dados):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO cadastros (nome, email, telefone, cpf, data_nascimento)
        VALUES (?, ?, ?, ?, ?)
    """, (dados['Nome'], dados['Email'], dados['Telefone'], dados['CPF'], dados['Data de Nascimento']))
    conn.commit()
    conn.close()
    print("Dados salvos com sucesso!")
