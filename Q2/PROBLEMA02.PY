
arquivo = open('Q2/medidas.txt','r')
med = arquivo.read()
listaMedi = list(med.split())



def contFreq(listaMedi):
	aux = 0 ; aux2 = 0
	for x in range (0,len(listaMedi)-1):
		if listaMedi[x] == listaMedi[x+1]:
				aux = aux + 1
		else:
				if(aux2<aux):
						aux2 = aux
	return aux2

a = contFreq(listaMedi)
print(a)
if '30M' == listaMedi[a]:
		cong = True
else:
    	cong = False

if cong == True:
	print((a-2) ,' medições de 30M')
else: 
	print((a-2) ,' medições de 40M')
