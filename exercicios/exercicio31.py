#Condicionais
#Exercicio 31
#Custo da viagem

distanciaviagem = int(input("Escreva a distancia da sua viagem em km: "))

if distanciaviagem <= 200:
    valor = distanciaviagem * 0.50
    print(f"A sua viagem de {distanciaviagem}km resultou em um valor total de R${valor}.")
else:
    valor = distanciaviagem * 0.45
    print(f"A sua viagem de {distanciaviagem}km resultou em um valor total de R${valor}.")