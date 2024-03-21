#Listas,tuplas,sets e dicionários.
#Exercicio 11
#Foram anotadas as idades e alturas de 30 alunos. 
#Faça um Programa que determine quantos alunos com mais de 13 anos 
#possuem altura inferior à média de altura desses alunos.
def media(alturas):
    return sum(alturas) / len(alturas)
cont = 0
dic = {}
alturas = []
for i in range (0,30):
    aluno = input("Digite o nome do aluno: ")
    altura = float(input("Digite a altura do aluno: "))
    idade = int(input("Digite a idade do aluno: "))
    dic[aluno] = {"Altura":altura, "Idade":idade}
    alturas.append(altura)
print(dic)
print(alturas)
media_altura = media(alturas)
print(media_altura)

print(f"A média de alturas é {media_altura}")
for aluno, dados in dic.items():
        if dados["Idade"] > 13 and dados["Altura"] < media_altura:
            cont += 1
print(f"O número de alunos com mais de 13 anos que possuem altura inferior à média é: {cont}")


