
arquivo = open('Q1/arquivo.txt','r')
med = arquivo.read()
lista = list(med.split())

print(lista)

valores = []
for val in lista:
    valores.append(int(val))


def faltante(lista,valueTotal):
    lst_return = []    
    
    for i in range(0,valueTotal): 
        lst_return.append(i+1)


    var = list(set(lst_return) - set(lista))
           
    return var

valueTotal = int(valores[0]);
del valores[0]
print(valores)
print(valueTotal)
if(valueTotal >=2 and valueTotal<=1000):
    print(faltante(valores,valueTotal))
else:
    print('Error')
