try:
    solucao = 50/int(input('Digite um numero: '))
    lista_a = [1,2]
    print(lista_a[int(input('Digite um numero do index: '))])
    # tudo que eu quero executar
except ZeroDivisionError as error:
    # tratamento de erro especifico ou generalizado
    print(f'Erro: {error} | Tente novamente com outro número')
#Pode ser aberto mais de um tratamento de erro
except IndexError as error:
    print(f'Erro: {error} | Este index não existe!')
except Exception as error:
    # tratamento de erro generalizado
    print(error)
else:
    print(f'Imprimir {solucao}')
    #alternativa que sera executada caso não de erro
