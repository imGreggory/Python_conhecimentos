#Laços e repetições
#Exercicio 55:
#Faça um programa que leia o peso de cinco pessoas.
#No final, mostre qual foi o maior e o menor peso lidos.
maior = 0
menor = 0
for p in range(1,6):
    peso = float(input(f"Digite o peso da pessoa {p}: "))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
            menor = peso
        

print(f"O peso da pessoa mais pesada é: {maior}\nO peso da pessoa menos pesada é: {menor}")