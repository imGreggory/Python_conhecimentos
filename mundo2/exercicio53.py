#Laços e repetições
#Exercicio 53
#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
#desconsiderando os espaços. 

frase = str(input("Digite uma frase e direi se ela é um palíndromo ou não:\nR: ")).upper()
frase_sem_espaco = ''.join(frase.split())
if frase_sem_espaco == frase_sem_espaco[::-1]:
    print("Sua frase é um palíndromo!")
else:
    print("Sua frase não é um palíndromo!")