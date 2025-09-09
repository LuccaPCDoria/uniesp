"""
Peça ao usuário para inserir três lados de um triângulo e determine se é um triângulo equilátero,
isósceles ou escaleno.
Triângulo Equilátero: Possui os três lados com medidas iguais.
Triângulo Isósceles: Possui dois lados com medidas iguais.
Triângulo Escaleno: Possui os três lados com medidas diferentes entre si.
"""

lado_1 = int(input("Digite o valor do primeiro lado: "))
lado_2 = int(input("Digite o valor do segundo lado: "))
lado_3 = int(input("Digite o valor do terceiro lado: "))

if lado_1 == lado_2 and lado_2 == lado_3:
    print("Isto é um triangulo equilátero")
elif lado_1 != lado_2 and lado_2 != lado_3:
    print("Isto é um triângulo Escaleno")
else:
    print("Isto é um triângulo Isósceles")

