import os

diretorio_atual = os.path.dirname(os.path.abspath(__file__))

imagem_entrada__nome = os.path.join(diretorio_atual, "imagem_original.jpg")
imagem_saida_nome = os.path.join(diretorio_atual, "imagem_copia.jpg")

if os.path.exists(imagem_entrada__nome):
    try:
        with open(imagem_entrada__nome, "rb") as imagem_entrada:
            with open(imagem_saida_nome, "wb") as imagem_saida:
                imagem_saida.write(imagem_entrada.read())
        print("Imagem copiada com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro ao copiar a imagem: {e}")

print(f"A imagem '{imagem_entrada__nome}' não foi encontrado na pasta.")