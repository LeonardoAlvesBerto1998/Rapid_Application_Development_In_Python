def exemplo3(caminho):
    with open(caminho,'w') as arquivo:
        arquivo.write('Esta é a primeira linha .\n')
        arquivo.write('Esta é a segunda linha .\n')


        linhas=['Esta é a primeira linha em uma lista .\n','esta é a segunda linha em uma lista.\n']
        arquivo.writelines(linhas)
    