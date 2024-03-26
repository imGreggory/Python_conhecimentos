#Condicionais
#Exercício Python 45: 
#Crie um programa que faça o computador jogar Jokenpô com você.

import random

pedrapapeltesoura = ["PEDRA", "PAPEL", "TESOURA"]
opcaodamaquina = random.choice(pedrapapeltesoura)
opcaodousuario = str(input("Bem vindo ao jogo de pedra papel e tesoura! escolha uma das opções e eu escolherei outra(Pedra, Papel ou Tesoura):\n")).upper().strip()
if opcaodousuario == "PEDRA" and opcaodamaquina == "TESOURA":
    print(f"Eu escolhi {opcaodamaquina}, você ganhou!")
elif opcaodousuario == "TESOURA" and opcaodamaquina == "PEDRA":
    print(f"Eu escolhi {opcaodamaquina}, você perdeu!")
elif opcaodousuario == "PEDRA" and opcaodamaquina == "PAPEL":
    print(f"Eu escolhi {opcaodamaquina}, você perdeu!")
elif opcaodousuario == "PAPEL" and opcaodamaquina == "PEDRA":
    print(f"Eu escolhi {opcaodamaquina}, você ganhou!")
elif opcaodousuario == "TESOURA" and opcaodamaquina == "PAPEL":
    print(f"Eu escolhi {opcaodamaquina}, você ganhou!")    
elif opcaodousuario == "TESOURA" and opcaodamaquina == "TESOURA":
    print(f"Eu escolhi {opcaodamaquina}, empatamos!")
elif opcaodousuario == "PAPEL" and opcaodamaquina == "PAPEL":
    print(f"Eu escolhi {opcaodamaquina}, empatamos!")
else: 
    print(f"Eu escolhi {opcaodamaquina}, empatamos!")    
