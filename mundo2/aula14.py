#Laços e repetições #2 (While)
#for c in range(1,10):
#    print(c)
#print("Fim!")
#c = 1
#while not c == 0:
#    c = int(input("Digite um número: "))
#print("Fim") 

n = 1
pares = impares = 0
while n != 0:
    n = int(input("Digite um número: "))
    if n != 0:
        if n % 2 == 0:
            pares += 1 
        else:
            impares += 1
print(f"A quantidade de números pares é de {pares} e a quantidade de números impares é de {impares}.")
