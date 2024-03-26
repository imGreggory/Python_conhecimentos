import random
numeros = []
def amplitude (maior, menor):
    return maior - menor


def main():
    for i in range (0,10):
        numero = round(random.uniform(1,50),0)
        numeros.append(numero)
    print(f"A lista de números é: {numeros}")
    maior = max(numeros)
    menor = min(numeros)
    amplitude(maior,menor)
    print(f"A amplitude dessa lista é de {amplitude(maior,menor)}")
main()
