#Condicionais
#Exercicio 36
#Aprovando empréstimo
#Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.


valordacasa = float(input('Escreva o valor da casa: '))
salario = float(input('Escreva seu salário: '))
totaldeanos = int(input('Em quantos anos você pretende pagar a casa? '))
prestacao = valordacasa / (totaldeanos * 12)
if prestacao > (salario * 0.30):
    print(f'Desculpa, mas o seu empréstimo não foi aprovado, pois o valor R${prestacao} da prestação superou 30% do seu salário.')
else:
    print(f'Parabéns! seu empréstimo de R${valordacasa} foi aprovado, o valor da sua prestação mensal é de R${prestacao}.')