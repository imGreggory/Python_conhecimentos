#Laços e repetições #2 (while)
#Exercicio 61:
#Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
#mostrando os 10 primeiros termos da progressão usando a estrutura while.
a1 = int(input("Digite o primeiro termo da progressão aritmética: "))
r = int(input("Digite a razão da progressão aritmética: "))
termo = a1
c = 1
while c < 11:
    print(f"{termo}", end=" -> ")
    termo += r
    c +=1
print("Fim!!")


    


    

