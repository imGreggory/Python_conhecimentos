#Laços e repetições #2 (while)
#Exercicio 62:
#Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
#O programa encerrará quando ele disser que quer mostrar 0 termos.
a1 = int(input("Digite o primeiro termo da progressão aritmética: "))
r = int(input("Digite a razão da progressão aritmética: "))
termo = a1
c = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c < total:
        print(f"{termo} -> ", end="")
        termo += r
        c +=1
    print("PAUSA")
    mais = int(input("Quantos termos a mais você quer mostrar? "))
print("Fim!!")



    


    

