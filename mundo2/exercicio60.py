#Laços e repetições #2 (while)
#Exercicio 60:
#Faça um programa que leia um número qualquer e mostre o seu fatorial.
numero = int(input("Digite um número: "))
cont = numero
f = 1
print(f"Calculando {numero}! = ", end="")
while cont > 0:
    print(f"{cont}", end="")
    print(" x " if cont > 1 else " = ", end="")
    f *= cont
    cont -= 1
print(f"{f}")

    


    

