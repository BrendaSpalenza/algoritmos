game = {'nome': 'LoL',
        'desenvolvedora': 'Riot',
         'ano': 2000}

print(game)


print(game['nome'])
print(game['desenvolvedora'])
print(game['ano'])

print(game.values())

for i in game.values():
    print(i)

for i in game.keys():
    print(i)
    print(game.items())

for i,j in game.items():  #Variável i pega os nomes das chaves, e a j pega os dados
    print('{} = {}' .format(i, j))