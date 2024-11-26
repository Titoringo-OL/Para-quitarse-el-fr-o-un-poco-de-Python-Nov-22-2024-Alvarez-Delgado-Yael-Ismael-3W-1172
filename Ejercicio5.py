print(" ")
print("Alvarez Delgado Yael Ismael 3W 1172")
print(" ")


def binario_a_entero(binario):
    try:
        return int(binario, 2)
    except ValueError:
        return "Error: No es un número binario válido"

binario = input("Introduce un número binario: ")

resultado = binario_a_entero(binario)

print(f"El número binario {binario} es igual a {resultado} en decimal.")
