#Listas,tuplas,sets e dicionários.
#Exercicio 09
#Faça um Programa que leia dois vetores com 10 elementos cada. 
#Gere um terceiro vetor de 20 elementos, 
#cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
vetor_A = []
vetor_B = []
vetor_C = []
for i in range (0,10):
    print("-="*30)
    numeroA = int(input("Digite um número para colocar na lista A: "))
    vetor_A.append(numeroA)
    print("-="*30)
    numeroB = int(input("Digite um número para colocar na lista B: "))
    vetor_B.append(numeroB)
for c in range (0,5):
    vetor_C.append(vetor_A[c])
    vetor_C.append(vetor_B[c])
print(vetor_A)
print(vetor_B)
print(vetor_C)




