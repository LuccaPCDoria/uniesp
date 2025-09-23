"""
Quantos valores pares existem entre 1 e 100
que sejam divisíveis por 5.
"""
import time
valorInicial = 1
contadorValores = 0
while valorInicial <= 100:

    if(valorInicial % 5) == 0 and (valorInicial % 2) == 0:
        contadorValores += 1
    valorInicial += 1
print(f'O número de divisíveis por 5 é {contadorValores}')

"""
Quanto seria 1 + 1 ?
"""

num1 = 1
num2 = 1
soma = num1 + num2
print(soma)

"""
alunos = ['Luiz H.', 'Duda', 'Mr. Fontanive', 'Thimenguista', 'Patrícia (Monitoria)', 'Aluna da minha esposa, Gabrial']

for aluno in alunos:
    print(f'Você é arretado(a) {aluno}.')
    time.sleep(2)
"""

i = 1000
contador = 0
while i <= 2000:
    if (i % 11) == 5:
        print(i)
        contador += 1

print(contador)











