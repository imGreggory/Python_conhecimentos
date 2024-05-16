from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Anthony', 10)
restaurante_praca.receber_avaliacao('Julio', 5)
restaurante_praca.receber_avaliacao('Gaby', 8)

def main():
    Restaurante.listar_restaurante()

if __name__ == '__main__':
    main()
