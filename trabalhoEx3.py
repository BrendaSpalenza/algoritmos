import random #Importa biblioteca de random

#Lista de nomes das pessoas que doaram
global listaDoacao
listaDoacao = []

#Função que adiciona nome na lista de doadores
def addDoacao(nome, valor):
    qtdVezesNaLista = valor // 10
    for i in range(qtdVezesNaLista):
        listaDoacao.append(nome)

#Lista de doadores com seus respectivos valores doados
addDoacao('Brenda', 5)
addDoacao('Ruth', 20)
addDoacao('Maria', 30)
addDoacao('Fernando', 50)


print('Lista normal: ')
print(listaDoacao)

random.shuffle(listaDoacao)
print('Lista embaralhada: ' )
print(listaDoacao)

sorteado = random.choice(listaDoacao)
print('Sorteado: ' + sorteado)







