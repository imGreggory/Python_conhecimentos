#Condicionais
#Exercicio 35
#analisando triangulo v1.0

reta1 = float(input("Escreva o valor da reta 1: "))
reta2 = float(input("Escreva o valor da reta 2: "))
reta3 = float(input("Escreva o valor da reta 3: "))

if reta3 > reta2 + reta1 and reta2 > reta1 + reta3 and reta1 > reta2 + reta3:
    print("As suas retas podem formar um triangulo")
else:
    print("As suas retas NÃO podem formar um triangulo")


