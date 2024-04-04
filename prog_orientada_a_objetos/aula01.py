class bicicleta:
    def __init__(self,cor,modelo,ano,valor): #método construtor
        self.cor = cor
        self.modelo = modelo
        self.ano = ano 
        self.valor = valor 
    def buzinar(self):
        print("Trim Trim")
    def parar(self):
        print("Parando a bicicleta...")
        print("Bicicleta parou.")
    def correr(self):
        print("Bicicleta começa a andar...")
        print("Bicicleta está correndo!")
    def get_cor(self):
        return self.cor

b1 = bicicleta("Vermelha", "Caloi", 2024, 600) #instância ou objeto
b1.buzinar()
b1.correr()
b1.parar()
print(b1.ano, b1.cor, b1.modelo, b1.valor)
print(b1.get_cor())



