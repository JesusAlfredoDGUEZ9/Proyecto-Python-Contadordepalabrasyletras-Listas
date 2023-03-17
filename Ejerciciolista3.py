#Crear un contador de palabras y letras de un texto.
#Mensaje.

print("Hola Bienvenid@. Este es un sistema de contador de palabras y letras. \nTendrás la oportunidad de saber el número de caracteres de tu texto y letras.")

print("\n")
#Ingresar el texto
texto = input("Ingresa tu texto:  ")
print("CONTADOR DE LETRAS.")
#Contador de palabras. Len sirve para contar en general.
print(f"La cantidad de letras de tu texto es de: {len(texto)}")
#Se crea una lista vacia
letra = []
#Pido al usuario que agregue una letra. Append sirve para agregar o almacenar.
letra.append(input("Agrega la letra que deseas buscar en el texto: "))
#Count sirve para saber cuantas veces se repite la palabra.
cantidad_letras = texto.count(letra[0])
#Imprimo el resultado.
print(f"La letra ''{letra[0]}'' se ha encontrado: {cantidad_letras}")


print("\n")
print("CONTADOR DE LETRAS.")
#Split sirve para separar.
palabras = texto.split()

print(f"En el texto existe {len(palabras)} palabras")





