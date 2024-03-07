#Condicionais
#Conversor de bases numéricas
#Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer 
#e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
import math

numero = int(input("Digite um número inteiro qualquer: "))
opcao = int(input("Para qual base númerica você quer converter o número? \n Se você quer converter para binário digite 1. \n Se você quer converter para octal digite 2. \n Se você quer converter para hexadecimal digite 3. \n Digite a alternativa: "))
numerobinario = bin(numero)
numerooctal = oct(numero)
numerohexadecimal = hex(numero)
if opcao == 1:
    print(f"Você escolheu a opção binário, vamos transformar o número {numero} em binário.")
    print(f"O número {numero} em binário é {numerobinario[2:]}")
if opcao == 2:
    print(f"Você escolheu a opção octal, vamos transformar o número {numero} em octal.")
    print(f"O número {numero} em octal é {numerooctal[2:]}")
if opcao == 3:
    print(f"Você escolheu a opção hexadecimal, vamos transformar o número {numero} em hexadecimal.")
    print(f"O número {numero} em hexadecimal é {numerohexadecimal[2:]}")

