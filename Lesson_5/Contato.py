class Contato:
    def __init__(self, nome, sobrenome, email, telefone):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.telefone = telefone

    def to_txt_format(self):
        """Converte o objeto Contato em uma linha de texto separada por ponto e vírgula."""
        return f"{self.nome};{self.sobrenome};{self.email};{self.telefone}\n"

    @classmethod
    def from_txt_format(cls, linha):
        """Cria um objeto Contato a partir de uma linha lida do arquivo .txt."""
        partes = linha.strip().split(";")
        if len(partes) == 4:
            return cls(partes[0], partes[1], partes[2], partes[3])
        return None

    def __str__(self):
        return f"{self.nome} {self.sobrenome} | E-mail: {self.email} | Telefone: {self.telefone}"