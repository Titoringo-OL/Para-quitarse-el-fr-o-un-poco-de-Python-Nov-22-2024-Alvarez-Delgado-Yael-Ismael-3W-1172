
def es_bisiesto(ano):
	if (ano%4 == 0):
		if (ano%100 != 0):
			print("Es bisiesto")
	else:
		print("No es bisiesto")

ano = int(input("Escriba un año para saber si es bisiesto: "))
es_bisiesto (ano)