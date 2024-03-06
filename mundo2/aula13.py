#Repetições FOR
#Aula 13
#i = int(input("Início: "))
#f = int(input("Fim: "))
#p = int(input("Passo: "))
#for c in range(i,f+1,p):
#   print(c)
#print("Fim.")

s = 0
for c in range(0,4):
    n = int(input("Escreva um número: "))
    s += n
print(f"O somatório dos números digitados foi de {s}")