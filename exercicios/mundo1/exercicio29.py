#Condicionais
#Exercicio 29
#Escreva um programa que leia a velocidade de um carro, se ele ultrapassar 80 km/h mostre
#uma mensagem dizendo que ele foi multado, a multa vai custar 7 reais por km acima da media.

velocidade = int(input("Escreva a velocidade do seu veículo em km/h: "))

if (velocidade > 80):
    multa = (velocidade - 80) * 7
    print(f"Atenção, sua velocidade foi de {velocidade}km/h e você foi multado por excesso de velocidade, sua multa foi de R${multa}, mais atenção por favor!")
else:
    print(f"Atenção, sua velocidade foi de {velocidade}km/h. Muito bem! você está dentro dos limites de velocidade, continue assim!")