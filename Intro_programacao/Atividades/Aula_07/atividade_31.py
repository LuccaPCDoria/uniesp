path = './path/'
# with faz abertura e fechamento de um recurso seja banco de dados, API ou leitura de arquivos
with open('arquivo.txt', 'r') as file_object:
    conteudo = file_object.read()
    print(conteudo)

