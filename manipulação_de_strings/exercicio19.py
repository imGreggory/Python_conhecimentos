#Importando Bibliotecas e módulos
#Exercicio 19
#Faça um programa que sorteie um aluno aleatorio dentre 4 alunos

from random import choice


aluno1 = str(input("Escreva o nome do primeiro aluno:"))
aluno2 = str(input("Escreva o nome do segundo aluno:"))
aluno3 = str(input("Escreva o nome do terceiro aluno:"))
aluno4 = str(input("Escreva o nome do quarto aluno:"))
listadealunos = [aluno1, aluno2, aluno3, aluno4]

print("O aluno sorteado foi: ", choice(listadealunos))




