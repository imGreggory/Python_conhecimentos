class restaurante:
    nome = 'Bistrô'
    categoria = '' 
    ativo = False

restaurante_praca = restaurante()
restaurante_praca.nome = "Praça"
restaurante_praca.categoria = "Gourmet"
restaurante_pizza = restaurante()
restaurante_pizza.nome = "Pizza Place"
restaurante_pizza.categoria = "Fastfood"
restaurante_pizza.ativo = True

restaurantes = [restaurante_praca, restaurante_pizza]
if restaurante_praca.ativo == False:
    print("O restaurante Praça está inativo")
else:
    print("O restaurante Praça está ativo")
print(restaurante_praca.nome, restaurante_praca.categoria)