
with open('medidas.txt','r') as arquivos:
	med = arquivos.read()
	print(med)
listaMedi = med.split()
print(listaMedi)

# totalMedi = int(input(''))	caso fosse digitar
# listaMedi = []
# for _ in range (totalMedi):
#     var = 0
#     var = input('Mediação: ')
#     listaMedi.append(var)

a = listaMedi.count('30M')
b = listaMedi.count('40M')

if a > b:
	print(a ,' medições de 30M')
else: 
	print(b ,' medições de 40M')
