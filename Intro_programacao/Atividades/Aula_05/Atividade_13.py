"""
Descrição:
Imagine que você é um mago que pode adivinhar o animal favorito das pessoas.
Crie um programa que pergunte à pessoa se seu animal favorito é mamífero ou réptil.
Se for mamífero, o programa deve sugerir que é um cachorro;
se for réptil, o programa deve sugerir que é uma tartaruga.
"""

tipoAnimal = input("Digite o tipo do seu animal: reptil ou mamifero\n").lower().strip()

if tipoAnimal == "mamifero":
    print("Seu animal seria um cachorro?")
elif tipoAnimal == "reptil":
    print("Seu animal seria uma tartaruga?")
else:
    print("Não sei que tipo de animal é este")
