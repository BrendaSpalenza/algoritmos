games = {'nome': ['Super mario', 'Zelda', 'Pokemon'],
         'videogame': ['Super Nitendo', 'Nitendo 64', 'Game Boy'],
         'ano': [1990, 1998, 1999]}
print(games)

#Mesmo exercício, so que via input

games = {'nome': [], 'videogame': [], 'ano': []}
for i in range(3):
    nome = input('Qual o nome do jogo?')
    videogame = input('Para qual videogame ele foi lançado?')
    ano = input('Qual o ano de lançamento?')
    games['nome'].append(nome)
    games['videogame'].append(videogame)
    games['ano'].append(ano)
print('-' * 20)
print(games)