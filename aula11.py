#print ('\33[7;30;41mOlá mundo!\033[m')
pergunta = int(input("O herick é:\n não binarie[1]\n cis[2]\n trans[3]\nAlternativa:"))
if pergunta == 1:
    print("Acertou! o Herick é não binarie")
elif pergunta == 2:
    print("Errou! o Herick não é cis")
elif pergunta == 3:
    print("Errou! o Herick não é trans(apesar de parecer)")
