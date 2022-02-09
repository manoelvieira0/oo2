class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes} Likes'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} Minutos - {self._likes} Likes'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} Temporadas - {self._likes} Likes'

class Playlist(list):
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    @property
    def listagem(self):
        return self._programas

    @property
    def tamanho(self):
        return len(self._programas)


vingadores = Filme("vingadores - guerra infinita", 2018, 160)
supernatural = Serie("supernatural", 2007, 15)
duna = Filme('duna', 2021, 130)
flash = Serie('flash', 2014, 6)

vingadores.dar_like()
vingadores.dar_like()
supernatural.dar_like()
supernatural.dar_like()
duna.dar_like()
duna.dar_like()
duna.dar_like()
flash.dar_like()

filmes_e_series = [vingadores, supernatural, duna, flash]

playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

print(f'Tamanho da Playlist: {len(playlist_fim_de_semana.listagem)}')

for programa in playlist_fim_de_semana.listagem:
    print(programa)


