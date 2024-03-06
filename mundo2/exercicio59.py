#Laços e repetições #2 (while)
#Exercicio 59:
#Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.
n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
opcao = 0
while opcao != 5:
    opcao = int(input("Digite a opção da ação desejada(1-5):\n[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa\nopção: "))
    if opcao == 1:
        soma = n1 + n2
        print(f"A soma dos números {n1} e {n2} é igual a {soma}")
        print('-='*20)
    elif opcao == 2:
        multi = n1 * n2
        print(f"A multiplicação dos números {n1} e {n2} é igual a {multi}")
        print('-='*20)
    elif opcao == 3:
        if n1>n2:
            maior = n1
            print(f"O número maior é o número {maior}")
            print('-='*20)
        elif n2>n1:
            maior = n2
            print(f"O número maior é o {maior}")
            print('-='*20)
        else:
            print(f"Os números são iguais.")
            print('-='*20)
    elif opcao == 4:
        n1 = float(input("Digite um número: "))
        n2 = float(input("Digite outro número: "))
        print('-='*20)
    elif opcao == 5:
        print("Obrigado por usar nossos serviços")
    else:
        print("Seu número não corresponde à nenhuma das opções, tente novamente!")

    

