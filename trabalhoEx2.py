def juntaNome(nome, sobrenome):
    primeiraLetra = nome[0]
    email = primeiraLetra.lower() + sobrenome.lower() + '05@algoritmos.com'
    print('Sra {} {}, seu email é {}' .format(nome, sobrenome, email))

#programa principal
nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')
juntaNome(nome, sobrenome)

