#Condicionais
#Exercicio 30
#Escreva um programa que leia um número inteiro, e diga se ele é par ou ímpar.

numero = int(input("Escreva um número inteiro: "))

if (numero % 2 == 0):
    print (f"Seu número é {numero} e ele é um número par!")
else: 
    print (f"Seu número é {numero} e ele é um número ímpar!")