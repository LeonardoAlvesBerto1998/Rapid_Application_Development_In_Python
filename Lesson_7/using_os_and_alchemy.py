import os
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column

DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
CAMINHO_BANCO = os.path.join(DIRETORIO_ATUAL, 'banco_dados.db')
engine = create_engine(f'sqlite:///{CAMINHO_BANCO}', echo=True)

#Criaçao da base declarativa atualizada (Padrão SQLAlchemy 2.0+)
class Base(DeclarativeBase):
    pass

#Definiçao da classe (modelo) utilizando Type Hints atuais (Mapped e mapped_column)
class Usuario(Base):
    __tablename__ = 'usuarios'

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column()
    idade: Mapped[int] = mapped_column()

    def __repr__(self) -> str:
        return f"Usuario(id{self.id}, nome={self.nome}, idade ={self.idade})"

#Criaçao das tabelas no banco de dados
Base.metadata.create_all(engine)

#Criaçao do gestor de sessoes
Session = sessionmaker(bind=engine)

#Utilizaçao do bloco 'width' (context manager) para garantir o fecho seguro da ligaçao
with Session() as session:
    #Inserçao de dados utilizando add_all para multiplos registros
    usuario1 = Usuario(nome='Raphael', idade=42)
    usuario2 = Usuario(nome='Leonardo', idade=28)
    session.add_all([usuario1, usuario2])

    #Efetivar alteraçoes
    session.commit()

    #Consulta de dados com a sintaxe atual (select em vez de query)
    stmt = select(Usuario)
    usuarios = session.scalars(stmt).all()

    for usuario in usuarios:
        print(usuario)