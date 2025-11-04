lista_filmes = [] # título, ano

def cadastrar_filme(l_filmes:list):
    titulo = input('Digite o nome do filme: ')
    ano = int(input('Digite o ano do filme: '))
    l_filmes.append([titulo, ano])
    return l_filmes

def visualizar_filmes(l_filmes:list):
    if len(l_filmes) > 0:
        for filme in l_filmes:
            print(f'{filme[1]} - {filme[0]}')
    else:
        print('Banco de filmes vazio!')
def salvar_arquivo_filmes(l_filmes:list):
    if len(l_filmes) > 0:
        try:
            with open('bd_filmes.txt', 'a', encoding='utf-8') as arquivo:
                for filme in l_filmes:
                    arquivo.write(f'{filme[1]}, {filme[0]}\n')
        except Exception as erro:
            print(f'Erro: {erro}')
        else:
            print('Filmes salvos com sucesso!')
    else:
        print('Banco de filmes vazio')
while True:

    print('-'*50)
    print('SISTEMA DE FILMES MELHOR QUE A NETFLIX')
    print('-' * 50)
    print('1 - Cadastrar Filme')
    print('2 - Visualizar Filmes')
    print('3 - Salvar Filmes')
    print('0 - Sair do sistema')

    op = int(input('Digite a opção desejada: '))

    if op == 1:
        print('--- Cadastro de Filmes ---')
        lista_filmes = cadastrar_filme(lista_filmes)

    elif op == 2:
        print('--- LISTA DE FILMES ---')
        visualizar_filmes(lista_filmes)

    elif op == 3:
        print('--- SALVAR FILMES ---')
        salvar_arquivo_filmes(lista_filmes)
    elif op == 0:
        print('Saindo do sistema...')
        break

    else:
        print('Opção inválida!')