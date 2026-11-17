from collections import namedtuple

Aluno=namedtuple("aluno",["nome","idade","trabalho"])
a1=Aluno("Leo",28,"Cientista de dados")
a2=Aluno('João',40,'Coveiro')
print(a1[1])
print(a1.nome)
print(a1.idade)
print(a1.trabalho)

print(a2)