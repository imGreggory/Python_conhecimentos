#Laços e repetições #3 (while/break)
#Exercicio 68
#Faça um programa que jogue par ou ímpar com o computador. 
#O jogo só será interrompido quando o jogador perder, 
#mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
import random
vitoria = 0
while True:
    escolha = input("Par ou impar? ").upper()
    if escolha == "PAR":
            print("Você escolheu par! muito bem, então fico com ímpar!")
            print("-="*15)
            escolha_usuario = int(input("Escolha um número inteiro de 0 a 10: "))
            escolha_maquina = random.randint(0,10)
            print(f"Eu escolhi o número {escolha_maquina} e você escolheu o número {escolha_usuario}")
            print("-="*15)
            if (escolha_maquina + escolha_usuario)%2 == 0:
                print(f"A soma dos números deu {escolha_usuario + escolha_maquina} que é par, parabéns você venceu!")
                print("-="*15)
                vitoria += 1
            else:
                print(f"A soma dos números deu {escolha_usuario + escolha_maquina} que é impar, Que pena, você perdeu.")
                print("-="*15)
                break
    elif escolha == "IMPAR":
            print("Você escolheu impar! muito bem, então fico com par!")
            print("-="*15)
            escolha_usuario = int(input("Escolha um número inteiro de 0 a 10:"))
            escolha_maquina = random.randint(0,11)
            print(f"Eu escolhi o número {escolha_maquina} e você escolheu o número {escolha_usuario}")
            print("-="*15)
            if (escolha_maquina + escolha_usuario)%2 == 0:
                print(f"A soma dos números deu {escolha_usuario + escolha_maquina} que é par, que pena, você perdeu!")
                print("-="*15)
                break 
            else:
                print(f"A soma dos números deu {escolha_usuario + escolha_maquina} que é impar, parabéns você venceu!")
                print("-="*15)
                vitoria += 1
    else:
        print("Escolha errada!")
print(f"O jogo acabou :( mas o usuario venceu {vitoria} vezes!")






    






