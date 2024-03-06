#Laços e repetições #2 (while)
#Exercicio 58:
#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. 
#Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
numeromaquina = randint(0,10)
numerousuario = int(input("Escreva um número de 0 a 10 que você acha que eu escolhi: "))
contador = 0
while numerousuario != numeromaquina:
    contador += 1
    if numerousuario < numeromaquina:
        numerousuario = (int(input("Você errou! O meu número é maior digite um número novamente: ")))
    if numerousuario > numeromaquina:
        numerousuario = (int(input("Você errou! O meu número é menor digite um número novamente: ")))
print(f"Parabéns, Você acertou! O número que eu escolhi foi {numeromaquina} e o número de tentativas até o acerto foi de {contador} tentativas.")




    

