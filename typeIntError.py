while True:
    try:
        x = int(input('Digite um número: '))
        break
    except ValueError:
        print('Oops! Número inválido. Tente novamente.... ')