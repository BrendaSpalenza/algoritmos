cadastro = {'nome': [], 'sexo': [], 'ano': []}

while True:
    terminar = input('Deseja cadastrar uma pessoa? [S/N]: ')
    if terminar.upper() in 'N':
        break
    if terminar .upper() not in 'S':
        print('Digite S para Sim e N para Não')
        continue

    nome = input('Qual o seu nome?')
    sexo = input('Qual o seu sexo [M/F]?')
    ano = int(input('Qual o seu ano de nascimento?'))
    cadastro['nome'].append(nome)
    cadastro['sexo'].append(sexo.upper())
    cadastro['ano'].append(ano)

print(cadastro)