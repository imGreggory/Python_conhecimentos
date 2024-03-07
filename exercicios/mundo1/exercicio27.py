#manipulação de Strings
#Exercicio 27
#faça um programa que leia o nome completo de uma pessoa mostrando em seguida o primeiro e o ultimo nome dessa pessoa.

n = str(input("Qual seu nome completo? ")).strip()
nome = n.split()
print(f"O seu nome completo é {n} seu primeiro nome é {nome[0]} e seu último nome é {nome[len(nome)-1]}.")