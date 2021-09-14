def numero(n):
    for i in range(n):
        num = i +1
        numString = str(num) + ' '
        print(numString * num)




x = int(input('Digite um número: '))
numero(x)