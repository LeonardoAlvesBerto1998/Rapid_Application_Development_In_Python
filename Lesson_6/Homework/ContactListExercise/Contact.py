import json
import os
from Contact_list import Contato

class ControleContatos:
    def __init__(self, arquivo="contatos.json"):
        self.arquivo = arquivo
        self._garantir_arquivo()

    def _garantir_arquivo(self):
        """Garante que o arquivo JSON exista com uma lista vazia caso não seja encontrado."""
        if not os.path.exists(self.arquivo):
            with open(self.arquivo, "w", encoding="utf-8") as f:
                json.dump([], f, ensure_ascii=False, indent=4)

    def carregar_contatos(self):
        """Lê os dados do arquivo JSON e retorna uma lista de objetos Contato."""
        if not os.path.exists(self.arquivo):
            return []
        
        with open(self.arquivo, "r", encoding="utf-8") as f:
            try:
                dados_lista = json.load(f)
                return [Contato.from_dict(d) for d in dados_lista]
            except json.JSONDecodeError:
                return []

    def salvar_contatos(self, contatos):
        """Salva a lista de objetos Contato convertendo-os para dicionários no arquivo JSON."""
        dados_lista = [c.to_dict() for c in contatos]
        with open(self.arquivo, "w", encoding="utf-8") as f:
            json.dump(dados_lista, f, ensure_ascii=False, indent=4)

    def adicionar(self, contato: Contato):
        """Adiciona um novo contato à lista e atualiza o arquivo."""
        contatos = self.carregar_contatos()
        contatos.append(contato)
        self.salvar_contatos(contatos)
        print(f"Sucesso: Contato de {contato.nome} adicionado!")

    def listar(self):
        """Retorna todos os contatos cadastrados."""
        return self.carregar_contatos()

    def buscar(self, termo):
        """Busca contatos por nome, sobrenome ou e-mail."""
        contatos = self.carregar_contatos()
        termo = termo.lower()
        resultados = [
            c for c in contatos 
            if termo in c.nome.lower() or termo in c.sobrenome.lower() or termo in c.email.lower()
        ]
        return resultados

    def remover(self, email):
        """Remove um contato com base no e-mail correspondente."""
        contatos = self.carregar_contatos()
        novos_contatos = [c for c in contatos if c.email.lower() != email.lower()]

        if len(contatos) == len(novos_contatos):
            print(f"Aviso: Nenhum contato encontrado com o e-mail '{email}'.")
            return False

        self.salvar_contatos(novos_contatos)
        print(f"Sucesso: Contato com e-mail '{email}' removido!")
        return True