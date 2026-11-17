from collections import defaultdict

def salas_de_aulas(estudantes: list, salas: list) -> dict:
    estudantes_por_sala = defaultdict(list)
    num_salas = len(salas)

    for i, estudante in enumerate(estudantes):
        #O indice da sala rotaciona: 0,1,0,1,0...
        sala_destino = salas[i % num_salas]
        estudantes_por_sala[sala_destino].append(estudante)
    return dict(estudantes_por_sala)

if __name__ == "__main__":
    alunos = ["Raphael", "Gilson", "Sara", "Vanessa", "Ana"]
    salas = ["307A", "308A"]
    print(salas_de_aulas(alunos, salas))