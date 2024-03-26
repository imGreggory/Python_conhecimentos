#Condicionais
#Exercício Python 040: 
#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#– Média abaixo de 5.0: REPROVADO
#– Média entre 5.0 e 6.9: RECUPERAÇÃO
#– Média 7.0 ou superior: APROVADO

nota1 = float(input("Escreva sua primeira nota: "))
nota2 = float(input("Escreva sua segunda nota: "))
media = (nota1 + nota2) / 2

if media < 5:
    print("Que pena! você foi reprovado, estude mais!")
elif 7 > media >= 5:
    print("Atenção! você ficou de recuperação, estude mais!")
else:
    print("Parabéns, você foi aprovado!")
