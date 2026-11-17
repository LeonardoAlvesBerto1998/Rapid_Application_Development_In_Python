from tkinter import ttk
import ArvorePessoa
import Pessoa

class Aplicativo:
    def __init__(self, raiz):
        raiz.title("Preview")
        raiz.geometry("500x400")
        
        self.gerenciador_arvore = ArvorePessoa()

        self.tabela = ttk.Treeview(raiz, columns=("nome", "idade"), show="headings")
        self.tabela.heading("nome", text="Nome")
        self.tabela.heading("idade", text="Idade")
        self.tabela.column("nome", width=330)
        self.tabela.column("idade", width=100, anchor="center")
        self.tabela.pack(fill="both", expand=True, padx=20, pady=20)

        self.inserir_dados_iniciais()

    def inserir_dados_iniciais(self):
        p1 = Pessoa("Ana", 20)
        p2 = Pessoa("Bruno", 29)

        self.gerenciador_arvore.adicionar(p1)
        self.gerenciador_arvore.adicionar(p2)

        self.inserir_arvore()

    def inserir_arvore(self):
        for pessoa in self.gerenciador_arvore.listar():
            self.tabela.insert("", "end", values=(pessoa.nome, pessoa.idade))