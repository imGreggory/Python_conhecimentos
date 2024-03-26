#Laços e repetições
#Exercício Python 48: 
#Faça um programa que calcule a soma entre todos os números que são múltiplos
#de três e que se encontram no intervalo de 1 até 500.

soma = 0
cont = 0
for c in range (1,501):
    if c % 3 == 0:
        soma += c
        cont += 1
print(f"a soma dos {cont} multiplos de 3 de 1 até 500 é: {soma}")

