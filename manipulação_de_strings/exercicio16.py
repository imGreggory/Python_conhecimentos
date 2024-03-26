#Importando Bibliotecas e módulos
#Exercicio 16
#Leia um numero quebrado e mostre a parte inteira dele usandoa  biblioteca math

from math import trunc

num = float(input("Escreva um número quebrado: "))
print(f"Seu número quebrado é {num} e ele sendo só a parte inteira é {trunc(num)}")

