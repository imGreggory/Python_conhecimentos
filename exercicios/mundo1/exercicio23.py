#manipulação de Strings
#Exercicio 23
#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.

numero = int(input("Escreva um número de 0 a 9999: "))
unidade = numero//1 % 10
dezena = numero//10 % 10
centena = numero//100 % 10
milhar = numero//1000 % 10
print(f"Milhar: {milhar}")
print(f"centena: {centena}")
print(f"dezena: {dezena}")
print(f"unidade: {unidade}")