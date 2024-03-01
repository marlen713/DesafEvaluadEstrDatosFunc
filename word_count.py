# Modos de apertura con la función open()
# Podemos abrir un archivo en modo de lectura con la letra r que viene de la palabra en inglés read que sígnica leer.

with open("lorem_ipsum.txt", "r") as file:
    texto = file.read()

#Los elementos de un set son único, lo que significa que no puede haber elementos duplicados.
#Split() Divide el texto en función de una string o carácter especificados y coloca cada fragmento en una celda independiente de la fila.
caracteres = len(set(texto))
palabras = len(set(texto.split(' ')))  


print(f"El número de caracteres distintos es: {caracteres} ")
print(f"El número de palabras distintas es: {palabras} ")

