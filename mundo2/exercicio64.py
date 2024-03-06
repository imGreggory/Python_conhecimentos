#Laços e repetições #2 (while)
#Exercicio 64:
# Crie um programa que leia vários números inteiros pelo teclado. 
#O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
#No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

n = 0
contador = 0
soma = 0
while n != 999:
    n = int(input("Escreva um número inteiro: "))
    if n != 999:
        soma = n + soma
        contador += 1
print(f"O TOTAL DE NÚMEROS DIGITADOS FORAM {contador} e a soma entre eles foi de {soma}")




