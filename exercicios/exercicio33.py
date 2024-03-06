#Condicionais
#Exercicio 33
#Maior e menor números

n1 = int(input("Escreva o primeiro número: "))
n2 = int(input("Escreva o segundo número: "))
n3 = int(input("Escreva o terceiro número: "))

maior = n1
if n2 > n3 and n2 > n1:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

menor = n2
if n1 < n2 and n1 < n3:
    menor = n1
if n3 < n1 and n3 < n2:
    menor = n3

print(f"O menor número é {menor} e o maior número é {maior}")