#Laços e repetições #2 (while)
#Exercicio 57:
#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. 
#Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = (input("Digite seu sexo: ")).strip().upper()[0]
while sexo not in 'MF':
    sexo = (input("Entrada inválida, informe novamente seu sexo (M / F): ")).strip().upper()[0]
print(f"O sexo digitado da pessoa é {sexo}.")    


    

