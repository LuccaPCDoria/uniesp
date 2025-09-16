"""
Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito.
Após, calcular e escrever o saldo atual (saldo atual = saldo - débito + crédito).
Também testar se saldo atual for maior ou igual a zero escrever a mensagem 'Saldo Positivo',
senão escrever a mensagem 'Saldo Negativo'.
"""

numeroDaConta = int(input("Digite o numero da sua conta: "))
saldo = int(input("Digite o saldo da sua conta: "))
debito = int(input("Digite o quanto entrou na sua conta: "))
credito = int(input("Digite o quanto saiu da sua conta: "))


saldoAtual = saldo + debito - credito

if saldoAtual >= 0:
    print("Saldo Positivo")
    print(saldoAtual)
else:
    print("Saldo Negativo")
    print(saldoAtual)
