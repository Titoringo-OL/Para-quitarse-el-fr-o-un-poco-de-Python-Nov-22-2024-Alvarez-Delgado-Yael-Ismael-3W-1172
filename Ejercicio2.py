def mas_larga(lista):
	palabra_mayor = len(lista[0])
	palabra_mostrar = lista[0]

	for palabra in lista:
		if palabra_mayor <= len(palabra):
			palabra_mostrar = palabra
			palabra_mayor = len(palabra)
		else:
			palabra_mostrar = palabra_mostrar

	print(palabra_mostrar)


lista = ["Salten", "Salten", "EstoEsRapReal"]
mas_larga(lista)