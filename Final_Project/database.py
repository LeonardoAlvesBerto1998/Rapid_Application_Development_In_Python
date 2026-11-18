import sqlite3
import datetime

def conectar():
    return sqlite3.connect('solicitacoes.db')

def criar_tabela():
    con = conectar()
    c = con.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS solicitacoes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        setor TEXT NOT NULL,
        quantidade INTEGER NOT NULL,
        material TEXT NOT NULL,
        prioridade TEXT NOT NULL,
        status TEXT NOT NULL,
        data_hora TEXT NOT NULL
        )
    ''')
    con.commit()
    con.close()

def cadastrar(setor, quantidade, material, prioridade):
    con = conectar()
    c = con.cursor()
    data_hora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    c.execute('''
        INSERT INTO solicitacoes(setor, quantidade, material, prioridade, status, data_hora)
        VALUES(?, ?, ?, ?, ?, ?)
    ''', (setor, quantidade, material, prioridade, 'Pendente', data_hora))
    con.commit()
    con.close()

def cobsultar_bdd():
    con = conectar()
    c = con.cursor()
    c.execute("SELECT * FROM solicitacoes")
    registros = c.fetchall()
    con.close()
    return registros

def atualizar_status(id_pedido, novo_status):
    con = conectar()
    c = con.cursor()
    c.execute("UPDATE solicitacoes SET status = ? WHERE id = ?", (novo_status, id_pedido))
    con.commit()
    con.close()

def pesquisar_filtrar(termo="", status_filtro="Todos"):
    con = conectar()
    c = con.cursor()
    query = "SELECT * FROM solicitacoes WHERE (setor LIKE ? OR material LIKE ?)"
    params = [f"%{termo}%", f"%{termo}%"]
    
    if status_filtro and status_filtro != "Todos":
        query += " AND status = ?"
        params.append(status_filtro)
        
    c.execute(query, params)
    registros = c.fetchall()
    con.close()
    return registros