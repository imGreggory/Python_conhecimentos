#Laços e repetições
#Exercicio 54:
#Crie um programa que leia o ano de nascimento de sete pessoas. 
#No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
contmaior = 0
contmenor = 0
for i in range (1, 8):
    idade = int(input(f"Digite a idade da pessoa {i}: "))
    if idade >= 18:
        contmaior += 1
    else: 
        contmenor += 1
print(f"{contmaior} já atingiu a maioridade.")
print(f"{contmenor} ainda não atingiu a maioridade.")

