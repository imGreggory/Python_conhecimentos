#Listas,tuplas,sets e dicionários.
#Exercicio 06
#Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
lista = []
soma = 0
multiplicacao = 1
for i in range(1,7):
    numero = int(input(f"Digite o {i}º número pra colocar na lista: "))
    lista.append(numero)
    soma += numero
    multiplicacao *= numero
print(lista)
print(soma)
print(multiplicacao)


