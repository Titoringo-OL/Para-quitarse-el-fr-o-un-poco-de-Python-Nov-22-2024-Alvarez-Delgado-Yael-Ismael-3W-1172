nombres = []
for x in range(1,10):
	nombres.append(input("Escribe un nombre: ").lower())

letra_buscada = (input("Qué letra buscas?: "))
cantidad = 0

for nombre in nombres:
	for letra in nombre:
		if letra == letra_buscada:
			cantidad = cantidad + 1
			break
		else:
			cantidad = cantidad
print (cantidad)