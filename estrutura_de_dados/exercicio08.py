#Listas,tuplas,sets e dicionários.
#Exercicio 08
#Faça um Programa que leia um vetor A com 10 números inteiros, 
#calcule e mostre a soma dos quadrados dos elementos do vetor.
vetor_A = []
soma = 0
for c in range (0,10):
    numero = int(input("Digite um número para por na lista: "))
    vetor_A.append(numero)
for i,numeros in enumerate(vetor_A):
    soma += numeros * numeros
print(soma)

