#Listas,tuplas,sets e dicionários.
#Exercicio 04
#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
#Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores
def main():
    lista = []
    i = 0
    while i < 10:
        numeros = int(input("Escreva uma letra para inserir na lista: "))
        lista.append(numeros)
        i +=1
    pares = []
    impares = []
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    print(f"lista de números pares: {pares}")
    print(f"lista de números impares: {impares}")   
main()