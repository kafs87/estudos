# 🧾 Desafio – Verificador de Números Pares e Ímpares
# 21/07/2025
# Autor: Kauan Ferreira da Silva

import os

def reset():
    resposta = None
    while True:
        resposta = input('Deseja verificar novamente? S/N: ')
        
        while resposta.lower() not in ('sim', 's', 'n', 'nao', 'não'):
            resposta = input('Resposta inválida. Deseja verificar novamente? S/N: ')
            
        if resposta.lower() in ('s', 'sim'):
            verificador()
            
        elif resposta.lower() in ('n', 'nao', 'não'):
            print('Até mais.')
            exit()     

def verificador():
    numero = None
    while numero != 0:
        try:
            numero = int(input('Digite um número inteiro ou "0" sair: '))
            
            if numero == 0:
                print('Até mais.')
                exit()
            elif numero % 2 == 0:
                print('Número par')
            elif numero % 2 != 0:
                print('Número ímpar')
        except ValueError:
            print("Erro: Por favor, insira valores numéricos válidos.\n")
            input("Pressione Enter para tentar novamente...")
            continue
        reset()
    
os.system('cls' if os.name == 'nt' else 'clear')
print('Verificador de números ímpares e pares')
verificador()