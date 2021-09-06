s1 = 'Algoritmos'
print(s1)
#s1[0]= 'a'  da erro, pois strings são imutaveis

s1 = list('Algoritmos')
print(s1) #print separado
print(''.join(s1)) #print agrupado

s1[0] = 'a'
print(''.join(s1))
