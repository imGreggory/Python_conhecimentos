class Musica:
    musicas = []
    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Musica.musicas.append(self)
    
    def __str__(self):
        return f"{self.nome}|{self.artista}|{self.duracao}"
    
    def listar_musica():
        for musica in Musica.musicas:
            print(f"Nome: {musica.nome}, Artista: {musica.artista}, duração: {musica.duracao}")

imagination = Musica("Imagination", "Forster The People", 255)

come_a_little_closer = Musica("Come a Little Closer", "Cage The Elephant", 187)

for_elise = Musica("For elise", "Saint Motel", 193)


Musica.listar_musica()



