#Laços e repetições #2 (while)
#Exercicio 65:
# Crie um programa que leia vários números inteiros pelo teclado. 
#No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
#O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
escolha = "S"
n = 0
soma = 0
maior = 0
menor = 0
cont = 0
while escolha == "S":
    n = int(input("Digite um número inteiro:"))
    if n > maior:
        maior = n
    soma += n
    escolha = input("Deseja continuar digitando?").upper()
    cont +=1
    if cont == 1:
        menor = n
    if n < menor:
        menor = n
media = soma / cont
print(f"Você digitou {cont} números e a media final dos números digitados é de {media} e o maior número foi {maior} e o menor é {menor}")
    






