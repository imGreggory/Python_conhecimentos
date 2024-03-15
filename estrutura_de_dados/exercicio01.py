#Listas,tuplas,sets e dicionários.
#exercicio 01
#Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
def main():
    vetor = []
    i = 0
    while i < 6:
        valor = int(input("Insira um valor no vetor:"))
        vetor.append(valor)
        i += 1
    print(vetor)

main()

