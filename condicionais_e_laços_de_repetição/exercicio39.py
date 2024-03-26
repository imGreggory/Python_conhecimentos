#Condicionais
#Exercicio 39
#alistamento militar

anoNascimento = int(input("Em que ano você nasceu? "))
idade = 2023 - anoNascimento

if idade == 18:
    print(f"Olá! você já possui {idade} anos, você já pode se alistar no serviço militar!")
elif idade < 18:
    print(f"Olá! você já possui {idade} anos, faltam {18-idade} anos para se alistar no serviço militar!")
else:
    print(f"Olá! você já possui {idade} anos, e você já passou {idade-18} anos da idade para se alistar no serviço militar, procure a unidade do exército mais próxima de você")
    
