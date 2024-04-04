class musica:
    nome = ""
    artista = ""
    duracao = int

imagination = musica()
imagination.nome = "imagination"
imagination.artista = "Forster The People"
imagination.duracao = 255

come_a_little_closer = musica()
come_a_little_closer.nome = "Come A Little Closer"
come_a_little_closer.artista = "Cage The Elephant"
come_a_little_closer.duracao = 187

for_elise = musica()
for_elise.nome = "For Elise"
for_elise.artista = "Saint Motel"
for_elise.duracao = 195

print(vars(come_a_little_closer))
print(vars(for_elise))
print(vars(imagination))
