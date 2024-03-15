#Listas,tuplas,sets e dicionários.
#Exercicio 05
#Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, 
#imprima o número de alunos com média maior ou igual a 7.0.
def media(notas):
    return (notas) / cont
alunos_aprovados = 0

lista_media = []
for i in range (0,3):
    print("-="*50)
    soma_notas = 0
    for cont in range (1,5):
        nota_aluno = float(input(f"Aluno número {i}! Digite sua {cont}ª nota: "))
        soma_notas += nota_aluno
    media_calculada = media(soma_notas)
    lista_media.append(media_calculada)
for i, medias in enumerate(lista_media):
    if medias >= 7:
        alunos_aprovados += 1
print(f"O número de alunos aprovados: {alunos_aprovados}")

