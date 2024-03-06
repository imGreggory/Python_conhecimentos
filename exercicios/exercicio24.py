#manipulação de Strings
#Exercicio 24
#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra "Santo"

cidade = str(input("Escreva o nome de uma cidade: "))
cidadecapitalizado = cidade.capitalize()
cidadedividido = cidadecapitalizado.split()
print('Santo' in cidadedividido[0])