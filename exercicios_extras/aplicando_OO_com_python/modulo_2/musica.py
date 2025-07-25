class Musica:
    musicas = []
    
    def __init__(self, nome, artista, duracao:int):    
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Musica.musicas.append(self)
        
    def listar_musicas():
        for musica in Musica.musicas:
            print(f"{musica.nome} | {musica.artista} | {musica.duracao}")
    
    
little_freak = Musica("Little Freak","Harry Styles", 194)
watermellon_sugar = Musica("Watermelon Sugar","Harry Styles", 185)

Musica.listar_musicas()