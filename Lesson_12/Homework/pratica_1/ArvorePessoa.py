import Pessoa

class ArvorePessoa:
    def __init__(self):
        self.lista_pessoas = []

    def adicionar(self, pessoa: Pessoa):
        self.lista_pessoas.append(pessoa)

    def listar(self):
        return self.lista_pessoas