#manipulação de Strings
#Exercicio 26
#Faça um programa que leia uma frase pelo teclado e diga:

frase = str(input("Escreva uma frase aleatória: ")).upper().strip()
#Quantas vezes aparece a letra 'a'

print(frase.count('A'))

#Em que posição ela aparece a primeira vez

print(f"A letra A vai aparecer primeiro na posição {frase.find('A') + 1}")


#Em que posição ela aparece a última vez
print(f"A letra A vai aparecer por ultimo na posição {frase.rfind('A') + 1}")