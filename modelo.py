class Filme:
    def __init__(self, nome, ano, duracao):
        self.nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.likes = 0

    def dar_like(self):
        self.likes += 1

class Serie:
    def __init__(self, nome, ano, temporadas):
        self.nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.likes = 0

    def dar_like(self):
        self.likes += 1

vingadores = Filme("vingadores - guerra infinita", 2018, 160)
vingadores.dar_like()
vingadores.dar_like()
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao} Minutos - Likes: {vingadores.likes}')

supernatural = Serie("supernatural", 2007, 15)
supernatural.dar_like()
print(f'Nome: {supernatural.nome} - Ano: {supernatural.ano} - Temporadas: {supernatural.temporadas} - Likes: {supernatural.likes}')

