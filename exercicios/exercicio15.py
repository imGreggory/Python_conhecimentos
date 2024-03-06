#Estruturas aritmeticas em python
#Exercicio 15
#Aluguel de carros

diasAlugado = int(input("Por quantos dias você alugou o carro? "))
kmRodado = float(input("Quantos Kilometros você percorreu com o carro? "))
precoPorDia = 60 * diasAlugado
precoPorKm = 0.15 * kmRodado
totalapagar = precoPorDia + precoPorKm

print(f"Você alugou o carro por {diasAlugado} dias e percorreu {kmRodado} kilometros, portanto o total a pagar pelo aluguel é de: {totalapagar} reais.")
