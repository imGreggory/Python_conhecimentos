#Listas,tuplas,sets e dicionários.
#Exercicio 07
#Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor.
#Imprima a idade e a altura na ordem inversa a ordem lida.
idades = []
alturas = []
for i in range (1,6):
    idade = int(input(f"Digite a {i}ª idade da lista: "))
    idades.append(idade)
    print("=-"*50)
    altura = float(input(f"Digite a {i}ª altura da lista: "))
    print("=-"*50)
    alturas.append(altura)
print(f"Lista de alturas: {alturas[::-1]} lista de idades: {idades[::-1]}")
