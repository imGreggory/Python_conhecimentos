#Listas,tuplas,sets e dicionários.
#Exercicio 03
#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
def main():
    lista = []
    i = 0
    while i < 10:
        caracteres = input("Escreva uma letra para inserir na lista: ").upper().strip()
        lista.append(caracteres)
        i +=1
    consoantes = []
    for caractere in lista:
        if caractere not in "AEIOU":
            consoantes.append(caractere)
    print(consoantes)
main()