#Laços e repetições #3 (while/break)
#Exercicio 70
#Crie um programa que leia o nome e o preço de vários produtos. 
#O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.
produto_mais_barato = ""
preco_produto_mais_barato = 0
cont = 0
total = 0
mais_que_mil = 0
while True:
    nomeproduto = input("Escreva o nome do produto: ")
    precoproduto = float(input("Escreva o preço do produto: "))
    escolha = input("Deseja continuar(S/N)? ").upper().strip()[0]
    if cont == 0:
        produto_mais_barato = nomeproduto
        preco_produto_mais_barato = precoproduto
    if precoproduto < preco_produto_mais_barato:
        produto_mais_barato = nomeproduto
        preco_produto_mais_barato = precoproduto
    if precoproduto > 1000:
        mais_que_mil += 1
    total += precoproduto
    if escolha in "N":
        print("Encerrando o programa.")
        break
    cont += 1
print(f"O produto mais barato é {produto_mais_barato} com o valor de {preco_produto_mais_barato}\nO valor total da compra foi R${total}\n{mais_que_mil} produtos custam mais que 1000 reais.")
print("Programa encerrado.")










    






