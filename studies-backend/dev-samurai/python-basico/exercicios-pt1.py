# Ex 1 - Calcule a soma dos numeros do 10 a0 14
soma = sum([10, 11, 12, 13, 14])
print(soma)

# Ex 2 - Calcule a média entre os numeros 10,15,20
media = sum([10, 15, 20]) / 2
print(media)

# Ex 3 - Peça para o usuário digitar duas notas de zero a dez e os pesos das notas e calcule a média ponderada entre elas. Obs: A soma dos pesos precisa ser dez.
nota1 = int(input('Digite a primeira nota de 0 a 10: '))
nota2 = int(input('Digite a segunda nota de 0 a 10: '))
peso1 = int(input('Digite quanto vale a segunda nota: '))
peso2 = int(input('Digite quanto vale a primera nota: '))

media_notas = (nota1 * peso1) + (nota2 * peso2) / (peso1+peso2)
print(f'A média das notas é: {media_notas}')

# Ex 4 - Qual o menor preço dessa lista?
# Preços: R$100.2, R$34.9, R$31.5, R$18.95

min_precos = min(100.2, 34.9, 31.5, 18.95)
print(min_precos)