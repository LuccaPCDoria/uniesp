nota1a = int(input("Digite a nota da 1a: "))
nota2a = int(input("Digite a nota da 2a: "))

media = (nota1a + nota2a) / 2

if media >= 6:
    print("Aluno aprovado!")
    print(f"Nota: {media}")
else:
    print("Aluno Reprovado!")
    print( f"Nota: {media}")

