texto = "Nossa aula manipulando string"

def exibir_string(texto):
    for i in range(len(texto)):
        print(texto[i])

def tamanho_string(texto):
    tamanho = len(texto)
    return tamanho

def contar_a(texto):
    contador = texto.count("a", 0, len(texto))
    return contador

def retornar_valores(texto):
    aula = texto.find("aula")
    return aula

def substituir_string(texto):
    novo_txt = texto.replace("aula", "zoom")
    return novo_txt


print(tamanho_string(texto))
print(contar_a(texto))
print(retornar_valores(texto))
print(substituir_string(texto))



print(texto.lower())
print(texto.upper())
print(texto.capitalize())
print(texto.title())
print(texto.swapcase())