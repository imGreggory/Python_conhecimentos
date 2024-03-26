#Laços e repetições #3 (while/break)
#Exercicio 67
#Faça um programa que mostre a tabuada de vários números, um de cada vez, 
#para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
while True:
    n = int(input("Escolha o número que deseja saber a tabuada(negativo para finalizar): ")) 
    if n < 0:
        print("Você digitou um número negativo, o programa irá encerrar!")
        break
    for c in range (1,11):
        print(f"{n} x {c} = {n*c}")
print("Acabou")

    






