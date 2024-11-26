
ano_curso = int(input("Escribe el año en curso: "))


nombre_uno = input("Primer nombre: ")
ano_uno = int(input(f"Año de nacimiento de {nombre_uno}: "))

nombre_dos = input("Segundo nombre: ")
ano_dos = int(input(f"Año de nacimiento de {nombre_dos}: "))

nombre_tres = input("Tercer nombre: ")
ano_tres = int(input(f"Año de nacimiento de {nombre_tres}: "))


cumple_uno = ano_curso - ano_uno
cumple_dos = ano_curso - ano_dos
cumple_tres = ano_curso - ano_tres


print(f"{nombre_uno} cumplirá {cumple_uno} años en el año {ano_curso}.")
print(f"{nombre_dos} cumplirá {cumple_dos} años en el año {ano_curso}.")
print(f"{nombre_tres} cumplirá {cumple_tres} años en el año {ano_curso}.")