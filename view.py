
import sqlite3 as lite
from datetime import datetime
from criarbd import*

# Inserir inventorio
def inserir_form(i):
    try:
        with con:
            cur = con.cursor()
            query = "INSERT INTO Inventario (nome, local, descricao, marca, data_da_compra, valor_da_compra, serie, imagem) VALUES (?,?,?,?,?,?,?,?)"
            cur.execute(query, i)
            print("Inserido com sucesso:", i)  # Log para confirmação
    except sqlite3.IntegrityError as e:
        print(f"Erro de integridade: {str(e)}")  # Erro específico de integridade
    except sqlite3.OperationalError as e:
        print(f"Erro operacional: {str(e)}")  # Erro operacional
    except Exception as e:
        print(f"Erro ao inserir no banco de dados: {str(e)}")  # Exibe o erro genérico

    #print(f"Executando consulta: {query} com os dados: {i}")
    #cur.execute(query, i)

# Deletar inventorio
def deletar_form(i):
   
    with con:
        cur = con.cursor()
        query = "DELETE FROM Inventario WHERE id=?"
        cur.execute(query, i)


# Atualizar inventorio
def atualizar_form(i):
    with con:
        cur = con.cursor()
        query = "UPDATE Inventario SET nome=?, local=?, descricao=?, marca=?, data_da_compra=?, valor_da_compra=?, serie=?, imagem=? WHERE id=?"
        cur.execute(query, i)


# Ver Inventario
def ver_form():
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Inventario")
        rows = cur.fetchall()
        for row in rows:
            lista_itens.append(row)
    return lista_itens


# Ver Iten no inventorio
def ver_item(id):
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Inventario WHERE id=?",(id))
        rows = cur.fetchall()
        for row in rows:
            lista_itens.append(row)
    return lista_itens
