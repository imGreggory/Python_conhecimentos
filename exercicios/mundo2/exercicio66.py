#Laços e repetições #3 (while/break)
#Exercicio 66:
# Crie um programa que leia números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

n = soma = cont = 0
while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    else:
        cont += 1
        soma += n
print(f"A soma dos seus {cont} números deu {soma}.")
    






