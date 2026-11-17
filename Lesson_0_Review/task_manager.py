class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.conclusion = False

    def is_done(self):
        self.conclusion = True

    def __str__(self):
        status = "✔" if self.conclusion else "✖"
        return f"[{status}] {self.title}: {self.description}"

class TaskManager:
    def __init__(self):
        self.tarefas = []

    def add(self, title, description):
        # Correção 1: 'Task' com T maiúsculo
        tarefa = Task(title, description)
        self.tarefas.append(tarefa)
        print(f"Tarefa '{title}' adicionada.")

    def list(self):
        if not self.tarefas:
            print("Sem tarefas.")
            return
        print("Lista: ")
        for idx, tarefa in enumerate(self.tarefas, 1):
            print(f"{idx}. {tarefa}")

    def estado(self, indice):
        if 0 < indice <= len(self.tarefas):
            # Correção 2: Chamando o método correto 'is_done()'
            self.tarefas[indice - 1].is_done()
            print(f"Tarefa {indice} concluida.")
        else: 
            print("Indice inexistente...")


if __name__ == "__main__":
    gerenciador = TaskManager()

    gerenciador.add("Ir ao shopping", "Pegar compras")

    gerenciador.list()

    gerenciador.estado(1)
    
    gerenciador.list()