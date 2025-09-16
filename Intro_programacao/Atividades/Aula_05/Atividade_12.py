"""
Descrição: Um guerreiro precisa de uma armadura especial para a batalha.
Para forjar a armadura, ele precisa de uma liga metálica que combina ferro e ouro.
O ferreiro diz que a liga precisa ter no mínimo 70% de ferro.
Crie um programa que receba a quantidade de ferro e ouro em kg e verifique se a porcentagem de ferro na liga é suficiente.
"""

qtdeFerro = float(input("Digite a quantidade de ferro em kg: "))
qtdeOuro = float(input("Digite a quantidade de ouro em kg: "))

liga = qtdeFerro + qtdeOuro
porcentagemFerro = qtdeFerro / liga * 100
porcentagemOuro = qtdeOuro / liga * 100

if porcentagemFerro >= 70:
    print("A quantidade de ferro na liga é suficiente")
else:
    print("A quantidade de ferro na liga é insuficiente")

print(f"Porcentagem de ferro na liga: {porcentagemFerro:.0f}%")
print(f"Porcentagem de Ouro na liga: {porcentagemOuro:.0f}%")
