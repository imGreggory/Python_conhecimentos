#Listas,tuplas,sets e dicionários.
#Exercicio 10
#Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
vetor_A = []
vetor_B = []
vetor_C = []
vetor_D = []
for i in range (0,5):
    print("-="*30)
    numeroA = int(input("Digite um número para colocar na lista A: "))
    vetor_A.append(numeroA)
    print("-="*30)
    numeroB = int(input("Digite um número para colocar na lista B: "))
    vetor_B.append(numeroB)
    print("-="*30)
    numeroC = int(input("Digite um número para colocar na lista C: "))
    vetor_C.append(numeroC)
for c in range (0,5):
    vetor_D.append(vetor_A[c])
    vetor_D.append(vetor_B[c])
    vetor_D.append(vetor_C[c])
print(vetor_A)
print(vetor_B)
print(vetor_C)
print(vetor_D)



