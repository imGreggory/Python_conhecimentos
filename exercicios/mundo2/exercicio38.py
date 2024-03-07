#Condicionais
#Exercicio 38
#Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#– O primeiro valor é maior
#– O segundo valor é maior
#– Não existe valor maior, os dois são iguais

numero1 = int(input("Escreva um número: "))
numero2 = int(input("Escreva outro número: "))

if numero1 > numero2:
    print("O primeiro valor é maior")
elif numero1 < numero2:
    print("O segundo valor é maior")   
else:
    print("Não existe valor maior, os dois são iguais") 
