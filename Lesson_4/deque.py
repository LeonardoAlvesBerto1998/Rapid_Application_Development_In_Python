from collections import deque

def gerenciar_historico(paginas: list, nova_pagina: str) -> deque:
    historico = deque(paginas, maxlen=3)
    print(f'Histórico inicial: {list(historico)}')
    historico.append(nova_pagina)
    print(f"Adicionando '{nova_pagina}' \n\n...\n Histórico agora: {list(historico)}")
    return historico

def gerenciar_fila_atendimento(nomes: list, prioritario: str) -> tuple:
    fila = deque(nomes)
    #Adiciona alguem no inicio da fila (prioridade)
    fila.appendleft(prioritario)
    #Remove quem está no fim da fila (o ultimo a chegar)
    #Em filas reais, geralmente usamos popleft() para atender o proimeiro.
    quem_saiu = fila.pop()
    return fila, quem_saiu

if __name__ == "__main__":
    paginas_visitadas = ["página 1", "página 2", "página 3"]
    mei_historico = gerenciar_historico(paginas_visitadas, "página 4")
    print("-"*30)
    clientes = ["Samira", "Juliana", "Caroline"]
    fila_final, atendido = gerenciar_fila_atendimento(clientes, "Aurora")
    print(f"Fila de espera: {list(fila_final)}")
    print(f"Usuário removido da ponta: {atendido}")