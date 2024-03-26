#Condicionais
#Exercício Python 44: 
#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal 
#– 3x ou mais no cartão: 20% de juros

valor = float(input("Insira o valor do produto: "))
modoPagamento = int(input("Qual o modo de pagamento?\n[1]À vista\n[2]Parcelado\n"))

if modoPagamento == 1:
    metodoPagamento = int(input("Qual o método de pagamento?\n[1]Dinheiro/cheque\n[2]Cartão\n"))
    if metodoPagamento == 1:
        print(f"Então escolheu o pagamento à vista no dinheiro/cheque! parabéns, você terá 10% de desconto!")
        valordinheirocheque = valor - (valor * 0.10)
        print(f"O valor da sua compra com desconto de 10% fica de R${valordinheirocheque}")

    else:
        print(f"Então escolheu o pagamento à vista no cartão! parabéns, você terá 5% de desconto!")
        valorcartaoavista = valor - (valor * 0.05)
        print(f"O valor da sua compra com desconto de 5% fica de R${valorcartaoavista}")
else:
    numeroparcelas = int(input("Você escolheu o modo de pagamento parcelado, informa em quantas parcelas deseja que o valor seja dividido: "))
    if numeroparcelas <= 2:
        parcela = valor / numeroparcelas
        print(f"O seu valor em {numeroparcelas} parcelas fica com o valor de R${parcela} cada parcela e o valor total de {valor}")
    else:
        valorcomjuros = valor + (valor *0.20 )
        parcela = (valorcomjuros) / numeroparcelas
        print(f"O seu valor em {numeroparcelas} parcelas fica com o valor de R${parcela} cada parcela, com o valor total das parcelas de R${valorcomjuros}.")



        
    


