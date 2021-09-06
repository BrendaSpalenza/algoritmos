from operator import itemgetter

lista = []
dic = {}


while True:
    dados = input('Digite 0 para encerrar o programa ou qualquer outra tecla para continuar.')
    if dados in '0':
        break
    codigo = int(input('Qual o código?'))
    estoque = int(input('Quantos tem no estoque?'))
    minimo = int(input('Qual o estoque mínimo necessario?'))
    lista.append({'codigo': codigo, 'estoque': estoque, 'minimo': minimo})

lista = sorted(lista, key=itemgetter('codigo'))

print('Encerrado')
print(lista)




