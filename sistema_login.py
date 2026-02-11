import sqlite3
    
def conectar_banco():
    return sqlite3.connect("banco.db")

def criar_tabela(conexao):
    cursor = conexao.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT,
        senha TEXT
    )
    """)
    conexao.commit()
    
def cadastrar_usuario(conexao):
    cursor = conexao.cursor()
    print("=== CADASTRO ===")
    usuario = input("Crie um usuario: ")
    senha = input("Crie uma senha: ")
    
    cursor.execute(
        "INSERT INTO usuarios (usuario, senha) VALUES (?, ?)",
        (usuario, senha)
    )
    conexao.commit()
    print("Usuario cadastrado com sucesso!")
    
def fazer_login(conexao):
    cursor = conexao.cursor()
    print("=== lOGIN ===")
    usuario = input("Usuario: ")
    senha = input("Senha: ")
    
    cursor.execute(
        "SELECT * FROM usuarios WHERE usuario = ? AND senha = ?",
        (usuario, senha)
    )
    
    return cursor.fetchone() is not None

def main():
    conexao = conectar_banco()
    criar_tabela(conexao)
    cadastrar_usuario(conexao)
    
    if fazer_login(conexao):
        print("Login realizado com sucesso!")
    else:
        print("Usuario ou senha incorretos")
        
    conexao.close()

main()
