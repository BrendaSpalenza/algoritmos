#Função que printa a nota e o conceito do aluno de acordo com os parâmetros passados.
def printaNotaEConceito(conceito, nota, aluno):
    print('O aluno(a) {} tirou a nota {} e se enquadra no conceito {}'.format(aluno, nota, conceito))

#Programa principal
while True:
    #Dados a serem inseridos
    dados = input('Inserir dados? 0-Não    1-Sim ')
    if dados in '0': #Obriga ao usuário a digitar 1 ou 0G
        break
    if dados not in '1':
        print('Por favor digite 1')
        continue

    aluno = input('Nome do aluno(a): ')
    nota = float(input('Nota final: '))

    if nota <= 2.9:
        printaNotaEConceito('E', nota, aluno)
    elif 3 <= nota <= 4.9:
        printaNotaEConceito('D', nota, aluno)
    elif nota >=5 and nota <= 6.9:
        printaNotaEConceito('C', nota, aluno)
    elif 7 <= nota <= 8.9:
        printaNotaEConceito('B', nota, aluno)
    elif 9 <= nota <= 10:
        printaNotaEConceito('A', nota, aluno)


