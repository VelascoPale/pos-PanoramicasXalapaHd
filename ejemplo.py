'''
def numbers(tres,cinco):
	lista = []
	for i in range(1,101):
		if i%tres==0:
			lista.append('Foo')
		else:
			lista.append(i)
		if i%cinco==0:
			lista.pop()
			lista.append('Bar')
		if i%(tres*cinco)== 0:
			lista.pop()
			lista.append('BarFoo')
	
	return lista
print(numbers(3,5))

'''
def multiplos(tres):
	lista = []
	for i in range(1,101):
		lista.append(i)
	for a in lista:
		if a%tres==0:
			lista[a] = 'Foo'
	return lista
print(multiplos(3))

