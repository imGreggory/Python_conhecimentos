#Laços e repetições
#Exercício Python 49: 
#Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

cont = 0
numero = int(input("Escreva o número que você deseja saber a tabuada: "))
for cont in range(-1,10):
    print(f"{cont + 1} x {numero} = {(cont + 1) * numero}")