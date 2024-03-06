#Importando Bibliotecas e módulos
#Exercicio 21
#Faça um programa que sorteie uma sequencia aleatoria de alunos dentre 4 alunos para apresentar um trabalho.

from random import shuffle


aluno1 = str(input("Escreva o nome do primeiro aluno:"))
aluno2 = str(input("Escreva o nome do segundo aluno:"))
aluno3 = str(input("Escreva o nome do terceiro aluno:"))
aluno4 = str(input("Escreva o nome do quarto aluno:"))
listadealunos = [aluno1, aluno2, aluno3, aluno4]
shuffle(listadealunos)

print("A ordem de apresentação será:")
print(listadealunos)





