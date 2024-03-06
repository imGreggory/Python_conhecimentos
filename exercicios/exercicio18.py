#Importando Bibliotecas e módulos
#Exercicio 18
#Faça um programa que leia os graus de um angulo e calcule o cos, sen e tan do angulo.

import math

angulo = float(input("Escreva os graus do angulo escolhido: "))
coseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
seno = math.sin(math.radians(angulo))

print(f"O angulo {angulo}° tem o cos de: {coseno:.2f}, o seno de: {seno:.2f} e a tangente de {tangente:.2f}")


