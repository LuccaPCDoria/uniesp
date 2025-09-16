"""
Um colecionador de moedas tem 3 tipos de moedas: de 1 real, de 50 centavos e de 25 centavos.
Escreva um programa que receba a quantidade de cada tipo de moeda e calcule o valor total que o colecionador tem.
"""

tipoA = float(input("Digite a quantidade de moedas de 1 real: "))
tipoB = float(input("Digite a quantidade de moedas de 50 centavos: ")) / 2
tipoC = float(input("Digite a quantidade de moedas de 25 centavos: ")) / 4

total = tipoA + tipoB + tipoC

print(f"O valor total das moedas é {total}")
