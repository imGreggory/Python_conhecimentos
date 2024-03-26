#manipulação de Strings
#Exercicio 22


nome = str(input("Escreva seu nome: "))

#O nome com todas as letras maiúsculas

print (f"Seu nome em letras maiúsculas é:{nome.upper()}")

#O nome com todas as letras minúscula

print(f"Seu nome em letras minúsculas é:{nome.lower()}")

#Quantas letras ao todo sem contar os espaços
nomesemespaco = nome.replace(' ', '')
print(f"O numero de caracteres do seu nome sem espaços é de: {len(nomesemespaco)}")

#Quantas letras tem o primeiro nome

nomedividido = nome.split()
print(f"O seu primeiro nome é {nomedividido[0]} e o número de caracteres do seu primeiro nome é de: {len(nomedividido[0])}")