print("---> Iniciando o Programa <---")

idade = int(input("Digite sua idade: "))

if idade < 17:
    print("Você pode entrar na festa!")
elif 16 <= idade < 18:
    print("É hora de voltar para sua casa!")
else:
    print("Vou chamar seus pais")