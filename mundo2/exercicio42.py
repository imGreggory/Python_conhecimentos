#Condicionais
#Exercício Python 42: 
#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#– EQUILÁTERO: todos os lados iguais
#– ISÓSCELES: dois lados iguais, um diferente
#– ESCALENO: todos os lados diferentes

reta1 = int(input("Escreva o valor da reta 1: "))
reta2 = int(input("Escreva o valor da reta 2: "))
reta3 = int(input("Escreva o valor da reta 3: "))

if reta3 < reta2 + reta1 and reta2 < reta1 + reta3 and reta1 < reta2 + reta3:
    print("As suas retas podem formar um triangulo! agora vamos ver que tipo de triângulo forma.")
    if reta1 == reta2 == reta3:
        print(f"O triângulo formado pelos valores {reta1}, {reta2}, {reta3} formam um triângulo equilátero.")
    elif reta1 != reta2 == reta3 or reta2 != reta1 == reta3 or reta3 != reta1 == reta2:
        print(f"O triângulo formado pelos valores {reta1}, {reta2}, {reta3} formam um triângulo isósceles.")
    elif reta1 != reta2 != reta3 != reta1:
        print(f"O triângulo formado pelos valores {reta1}, {reta2}, {reta3} formam um triângulo escaleno.")
    else:
        print("Tente novamente!")
else:
    print("As suas retas NÃO podem formar um triangulo")

