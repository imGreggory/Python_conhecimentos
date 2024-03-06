#Laços e repetições
#Exercício 52
#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
numero = int(input("Escreva um número inteiro no qual deseja saber se é primo: "))
contagem = 0
for c in range (2, numero + 1):
    if numero % c == 0:
        contagem += 1
        if contagem > 1:
            break
if contagem > 1:
    print("Seu número não é primo")
else: 
    print("Seu número é primo")