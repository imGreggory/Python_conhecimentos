#Listas,tuplas,sets e dicionários.
#Exercicio 02
#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

def main():
    lista = []
    i = 0
    while i < 6:
        numero = int(input("Insira um valor na lista: "))
        lista.append(numero)
        i += 1
    print(lista)
    print(lista[::-1])

main()