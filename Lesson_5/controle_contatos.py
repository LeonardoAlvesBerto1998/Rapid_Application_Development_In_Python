import os
import Contato

class ControleContatos:
    def __init__(self, arquivo="contatos.txt"):
        self.arquivo = arquivo
        self._garantir_arquivo()

    def _garantir_arquivo(self):
        """Garante que o arquivo .txt exista para evitar erros de leitura."""
        if not os.path.exists(self.arquivo):
            open(self.arquivo, "w").close()

    def adicionar(self, contato: Contato):
        """Adiciona um novo contato ao final do arquivo."""
        with open(self.arquivo, "a", encoding="utf-8") as f:
            f.write(contato.to_txt_format())
        print(f"Sucesso: Contato de {contato.nome} adicionado!")

    def listar(self):
        """Retorna todos os contatos cadastrados."""
        return self.carregar_todos()

    def buscar(self, termo):
        """Busca contatos por nome, sobrenome ou e-mail."""
        contatos = self.carregar_todos()
        termo = termo.lower()
        encontrados = [
            c for c in contatos 
            if termo in c.nome.lower() or termo in c.sobrenome.lower() or termo in c.email.lower()
        ]
        return encontrados

    def remover(self, email):
        """Remove um contato com base no e-mail (chave única)."""
        contatos = self.carregar_todos()
        novos_contatos = [c for c in contatos if c.email.lower() != email.lower()]

        if len(contatos) == len(novos_contatos):
            print(f"Aviso: Nenhum contato encontrado com o e-mail '{email}'.")
            return False

        # Reescreve o arquivo sem o contato removido
        with open(self.arquivo, "w", encoding="utf-8") as f:
            for c in novos_contatos:
                f.write(c.to_txt_format())
        
        print(f"Sucesso: Contato com e-mail '{email}' removido!")
        return True

    def carregar_todos(self):
        """Lê o arquivo .txt e converte todas as linhas em objetos Contato."""
        contatos = []
        if os.path.exists(self.arquivo):
            with open(self.arquivo, "r", encoding="utf-8") as f:
                for linha in f:
                    linha = linha.strip()
                    if linha:
                        contato = Contato.from_txt_format(linha)
                        if contato:
                            contatos.append(contato)
        return contatos