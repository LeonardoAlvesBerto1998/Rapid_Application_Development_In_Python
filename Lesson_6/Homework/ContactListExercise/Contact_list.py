#Crie uma classe chamada Contato para representar um contato com informações como
#nome, sobrenome, email e telefone. Em seguida, crie uma classe ControleContatos 
#que permite adicionar, buscar e remover contatos, agora utilizando txt e json 
#para manipular dados.  

import os

class Contato:
    def __init__(self, nome, sobrenome, email, telefone):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.telefone = telefone

    def to_dict(self):
        """Converte o objeto Contato em um dicionário para serialização JSON."""
        return {
            "nome": self.nome,
            "sobrenome": self.sobrenome,
            "email": self.email,
            "telefone": self.telefone
        }

    @classmethod
    def from_dict(cls, dados):
        """Cria um objeto Contato a partir de um dicionário carregado do JSON."""
        return cls(
            dados.get("nome"),
            dados.get("sobrenome"),
            dados.get("email"),
            dados.get("telefone")
        )

    def __str__(self):
        return f"{self.nome} {self.sobrenome} | E-mail: {self.email} | Telefone: {self.telefone}"