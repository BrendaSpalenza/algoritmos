#item = []
#mercado = []

# for i in range(3):
#     item.append(input('Digite o nome do produto: '))
#     item.append(input('Digite a quantidade do produto: '))
#     item.append(input('Digite o valor do produto: '))
#     mercado.append(item[:])
#     item.clear()   #Serve para que eu povoe uma lista de item e limpe ela depois para reiniciar novamente o processo
# print(mercado)



#Modo mais simples

mercado = []

for i in range(3):
    nome = input('Digite o nome do produto: ')
    qtd = int(input('Digite a quantidade: '))
    valor = float(input('Digite o preço: '))
    mercado.append([nome, qtd, valor])
print(mercado)