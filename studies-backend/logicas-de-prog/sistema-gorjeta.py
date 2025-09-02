# 🧾 Desafio – Calculadora de Gorjeta
# 31/08/2025
# Autor: Kauan Ferreira da Silva

valor_conta = int(input('Insira o valor a pagar da conta: '))
percentual = int(input('Insira a porcentagem que deseja deixar: '))
porcentagem = percentual * 0.01
gorjeta = valor_conta * porcentagem


print(f'O valor da gorjeta será de: {gorjeta}')