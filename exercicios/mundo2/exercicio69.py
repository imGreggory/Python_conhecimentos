#Laços e repetições #3 (while/break)
#Exercicio 69
#Crie um programa que leia a idade e o sexo de várias pessoas.
#A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.
homens = 0
mulheres = 0
mais_dezoito = 0
while True:
    print("----------------Cadastro----------------")
    idade = int(input("Digite a idade da pessoa: "))
    sexo = input("Digite o sexo da pessoa(M/F): ").strip().upper()[0]
    if idade > 18:
        mais_dezoito += 1
    if sexo in "M":
        homens += 1
    if sexo in "F":
        if idade < 20:
            mulheres += 1
    escolha = input("Deseja continuar cadastrando(S/N)?").strip().upper()[0]
    if escolha in "N":
        break
print(f"Cadastro de pessoas finalizado!\nHá {mais_dezoito} pessoas com mais de 18 anos.\nHá {homens} homens cadastrados.\nHá {mulheres} mulhers  com menos de 20 anos cadastradas.")







    






