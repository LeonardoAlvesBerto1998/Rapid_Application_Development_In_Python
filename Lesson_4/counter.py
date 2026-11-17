from collections import Counter

def funcao_corta_palavras(texto:str) -> int:
    palavras = texto.split()
    contagem = Counter(palavras)
    return contagem

if __name__ == "__main__":
    texto = 'maçã banana maçã laranja banana maçã'
    print(funcao_corta_palavras(texto))
    print(funcao_corta_palavras(texto).most_common(2))