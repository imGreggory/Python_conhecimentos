#Laços e repetições
#Exercício Python 50: 
#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas 
#daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
somapares = 0
for c in range (0,6):
    numero = int(input("Escreva um número inteiro: "))
    if numero % 2 == 0:
        somapares += numero
print(f"A soma dos números pares digitados é de: {somapares}")
        
