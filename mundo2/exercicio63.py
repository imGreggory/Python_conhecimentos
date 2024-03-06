#Laços e repetições #2 (while)
#Exercicio 63:
# Escreva um programa que leia um número N inteiro qualquer
# e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.

n = int(input("Escreva um número inteiro: "))
contador = 0
ultimo = 0
penultimo = 1
while contador < n:
    termo = ultimo + penultimo
    penultimo = ultimo
    ultimo = termo
    print(f"{termo} -> ", end="")
    contador += 1
print("Fim!!")



