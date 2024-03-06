#Condicionais
#Exercicio 28
#jogo de advinhação de numero

import random

numeromaquina = random.randrange(0,5)

numerousuario = int(input("Escreva um número de 0 a 5: "))

if numerousuario == numeromaquina:
    print(f"O numero escolhido pela máquina foi {numeromaquina} e o seu número foi: {numerousuario}, parabéns você ganhou!")
else: 
    print(f"O numero escolhido pela máquina foi {numeromaquina} e o seu número foi: {numerousuario}, você perdeu! tente denovo")

