class Filme:
    def __init__(self, nome, ano, duracao):
        self.nome = nome
        self.ano = ano
        self.duracao = duracao

class Serie:
    def __init__(self, nome, ano, temporadas):
        self.nome = nome
        self.ano = ano
        self.temporadas = temporadas

vingadores = Filme("Vingadores - Guerra Infinita", 2018, 160)
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao} Minutos')

supernatural = Serie("Supernatural", 2007, 15)
print(f'Nome: {supernatural.nome} - Ano: {supernatural.ano} - Temporadas: {supernatural.temporadas}')