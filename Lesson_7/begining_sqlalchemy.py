from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Conectando a um banco sqlite em memoria
engine = create_engine('sqlite:///:memory:', echo=True)

#Criaçao da base declarativa
base = declarative_base()

#Definindo a classe (modelo) Usuario
class Usuario(base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)

    def __repr__(self):
        return f"Usuario(id={self.id}), nome={self.nome}, idade={self.idade})"

#Criaçao das tabelas do banco de dados
base.metadata.create_all(engine)

#criaçao de uma sessao
Session = sessionmaker(bind=engine)
session = Session()

#Inserçao de dados
usuario1 = Usuario(nome='Raphael', idade = 42)
usuario2 = Usuario(nome='Leonardo', idade = 28)
session.add(usuario1)
session.add(usuario2)

#comit das alteraçoes
session.commit()

#Consulta de dados
usuarios = session.query(Usuario).all()
for usuario in usuarios:
    print(usuario)