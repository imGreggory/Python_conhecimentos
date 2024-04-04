class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self._nome = nome
        self._categoria = categoria 
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f"{self._nome}|{self._categoria}"
    
    @property
    def ativo(self):
        return "Está ativo" if self._ativo else "Está desativado"
    
    @classmethod
    def listar_restaurante(cls):
        print(f"{"Nome do Restaurante".ljust(25)}|{"Categoria".ljust(25)} |{"Status".ljust(25)}")
        for restaurante in Restaurante.restaurantes:
            print(f"{restaurante._nome.ljust(25)}|{restaurante._categoria.ljust(25)} | {restaurante.ativo.ljust(25)}")
    
    def alternar_estado(self):
        self._ativo = not self._ativo

restaurante_praca = Restaurante("Praça", "Gourmet")
restaurante_praca.alternar_estado()
restaurante_pizza = Restaurante("Pizza Place", "Italiana")
restaurante_pizza._nome = "Pizza Place"
restaurante_pizza._categoria = "Fastfood"


Restaurante.listar_restaurante()


