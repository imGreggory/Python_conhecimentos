#Condicionais
#Exercicio 34
#Aumentos multiplos

salario = int(input("Escreva seu salário: "))

if salario > 1250:
    salarionovo = salario + (salario * 0.10)
    print(f"O seu salário é R${salario} e recebeu um aumento de 10% totalizando R${salarionovo}")
else: 
    salarionovo = salario + (salario * 0.15)
    print(f"O seu salário é R${salario} e recebeu um aumento de 15% totalizando R${salarionovo}")
    
