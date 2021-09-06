# games = []
# game1 = {'nome': 'Super Mario',
#          'videogame': 'Super Nitendo',
#           'ano': 1990}
# game2 = {'nome': 'Zelda Ocarina of Time',
#          'videogame': 'Nitendo 64',
#          'ano': 1998 }
# game3 = {'nome': 'Pokemon Yellow',
#         'videogame': 'Game Boy',
#         'ano': 1999}
# games = [game1, game2, game3]
# print(games)
#
# print('\n')

#Criando a lista via input

game = {}
games = []
for i in range(3):
    game['nome'] = input('Qual o nome do jogo?')
    game['videogame'] = input('Qual o videogame?')
    game['ano'] = input('Qual ano ele foi lançado?')
    games.append(game.copy())
print('-' * 20)
for e in games:
    for i, j in e.items():
        print('O campo {} tem o valor {}.' .format(i,j))