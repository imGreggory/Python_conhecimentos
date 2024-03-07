#Importando Bibliotecas e módulos
#Exercicio 17
#Leia o cateto oposto e o adjacente de um triangulo e calcule a hipotenusa do mesmo.

from math import hypot

catad = float(input("Escreva o tamanho do cateto adjacente: "))
catopo = float(input("Escreva o tamanho do cateto oposto: "))
hipotenusa = hypot(catad, catopo)
print(f"A sua hipotenusa tem o tamanho de: {hipotenusa:.2f}")


