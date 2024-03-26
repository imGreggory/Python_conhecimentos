#Laços e repetições
#Exercicio 56:
#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo,
#qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
cont_idade_mulheres = 0
cont_idade_homens = 0

cont_media = 0
cont_pessoas = 0
nome_mais_velho = ""
for p in range (1,5):
    print(20*"-=")
    nome = str(input("Digite o nome da pessoa digitada: \n"))
    idade = int(input("Digite a idade da pessoa desejada: \n"))
    sexo = str(input("Deseje o sexo da pessoa desejada('M' ou 'F'): \n")).upper()
    cont_media += idade
    cont_pessoas += 1
    if sexo == "F" and idade < 20:
        cont_idade_mulheres += 1
    if sexo == "M" and idade > cont_idade_homens:
        nome_mais_velho = nome
        cont_idade_homens = idade
media = cont_media / cont_pessoas
print(f"A media de idade das pessoas digitadas é de {media}")
print(f"A quantidade de mulheres com menos de 20 anos é de {cont_idade_mulheres} mulheres")
if nome_mais_velho != "":
    print(f"O nome do homem mais velho da lista é {nome_mais_velho}")
else:
    print(f"Nenhum homem foi informado")

    

