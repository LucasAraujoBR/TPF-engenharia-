
arquivo = open('Q2/medidas.txt','r')
med = arquivo.read()
listaMedi = list(med.split())

a = listaMedi.count('30M')
b = listaMedi.count('40M')

if a > b:
	print(a ,' medições de 30M')
else: 
	print(b ,' medições de 40M')
