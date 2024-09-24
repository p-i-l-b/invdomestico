
import sqlite3 as lite

con = lite.connect('dados.db')

# Teste de conexão
try:
    con.execute("SELECT 1")
    print("Conexão com o banco de dados bem-sucedida.")
except Exception as e:
    print(f"Erro ao conectar ao banco de dados: {str(e)}")

with con:
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Inventario (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    local TEXT,
                    descricao TEXT,
                    marca TEXT,
                    data_da_compra TEXT,
                    valor_da_compra REAL,
                    serie TEXT,
                    imagem TEXT)''')


# def verificar_tabela():
#     cur = con.cursor()
#     cur.execute("PRAGMA table_info(Inventario)")
#     colunas = cur.fetchall()
#     print("Colunas na tabela 'Inventario':")
#     for coluna in colunas:
#         print(coluna)
# verificar_tabela()

def teste_inserir():
    con = lite.connect('dados.db')
    with con:
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS Inventario (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT,
                        local TEXT,
                        descricao TEXT,
                        marca TEXT,
                        data_da_compra TEXT,
                        valor_da_compra REAL,
                        serie TEXT,
                        imagem TEXT)''')
        query = "INSERT INTO Inventario (nome, local, descricao, marca, data_da_compra, valor_da_compra, serie, imagem) VALUES (?,?,?,?,?,?,?,?)"
        cur.execute(query, ('Teste', 'Sala', 'Descrição', 'Marca', '9/24/24', 0.0, 'A123456', 'item.png'))
teste_inserir()
