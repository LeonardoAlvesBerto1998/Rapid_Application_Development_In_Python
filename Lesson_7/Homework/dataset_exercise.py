#Usando a documentação, faça um pequeno controle de contatos apenas com nome e telefone...
#Crie um C.R.I.D. (Create, Read, Update, Delete) mas faça apenas usando a documentação.
#https://dataset.readthedocs.io/en/latest/

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, select, update, delete

engine = create_engine('sqlite:///contatos.db', echo=False)
metadata = MetaData()

contato_table = Table(
    "contato",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("nome", String),
    Column("telefone", String)
)

metadata.create_all(engine)

def criar_contato(nome, telefone):
    with engine.begin() as conn:
        stmt = contato_table.insert().values(nome=nome, telefone=telefone)
        conn.execute(stmt)
    print(f"Sucesso: Contato '{nome}' criado!")

def ler_contatos():
    print("\n--- Lista de Contatos ---")
    with engine.connect() as conn:
        stmt = select(contato_table)
        contatos = conn.execute(stmt).fetchall()
    
    if not contatos:
        print("Nenhum contato cadastrado.")
    for c in contatos:
        print(f"ID: {c.id} | Nome: {c.nome} | Telefone: {c.telefone}")
    print("-" * 25)

def atualizar_contato(id_contato, novo_nome, novo_telefone):
    with engine.begin() as conn:
        stmt = update(contato_table).where(contato_table.c.id == id_contato).values(nome=novo_nome, telefone=novo_telefone)
        conn.execute(stmt)
    print(f"Sucesso: Contato ID {id_contato} atualizado!")

def deletar_contato(id_contato):
    with engine.begin() as conn:
        stmt = delete(contato_table).where(contato_table.c.id == id_contato)
        conn.execute(stmt)
    print(f"Sucesso: Contato ID {id_contato} removido!")

if __name__ == "__main__":
    with engine.begin() as conn:
        contato_table.drop(conn, checkfirst=True)
        metadata.create_all(conn)

    criar_contato("Leonardo", "96947-1234")
    criar_contato("José das Couves", "97070-7070")

    ler_contatos()

    atualizar_contato(1, "Ana", "99999-0000")

    ler_contatos()

    deletar_contato(2)

    ler_contatos()