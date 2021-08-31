preco = float(input('Digite o preço do produto:'))
p = float(input('Digite o percentual de desconto (0-100)%:'))

desconto = preco * (p / 100)
final = preco - desconto


print('O preço do produto é {}. O desconto será de {}%.' .format(preco, p))
print('O valor calculado de desconto: {}. Valor final do produto: {}.' .format(desconto, final))