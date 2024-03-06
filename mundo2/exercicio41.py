#Condicionais
#Exercício Python 041: 
#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#– Até 9 anos: MIRIM
#– Até 14 anos: INFANTIL
#– Até 19 anos: JÚNIOR
#– Até 25 anos: SÊNIOR
#– Acima de 25 anos: MASTER


idade = int(input("Qual a idade do atleta?\n"))
if idade <= 9:
    print("O atleta está classificado na categoria MIRIM.")
elif  14 >= idade > 9:
    print("O atleta está classificado na categoria INFANTIL.")
elif  19 >= idade > 14:
    print("O atleta está classificado na categoria JÚNIOR.")
elif  25 >= idade > 19:
    print("O atleta está classificado na categoria SÊNIOR.")
elif idade > 25:
    print("O atleta está classificado na categoria MASTER.")

    