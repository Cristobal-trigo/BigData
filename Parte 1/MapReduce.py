def Map(nombre_archivo):
    archivo_letra = open(nombre_archivo)
    lista = []
    for linea in archivo_letra:
        if linea != "\n":
            linea = linea.strip().strip(",?").split()
            for elemento in linea:
                lista.append((elemento.lower(), 1))

    archivo_letra.close()
    return lista

def ShuffleSort(lista):
    lista_ordenada = []
    for palabra in lista:
        bandera = True
        for elemento in lista_ordenada:
            if palabra[0] == elemento[0]:
                elemento[1].append(1)
                bandera = False

        if bandera:
            lista_ordenada.append([palabra[0], [1]])

    return lista_ordenada

def Reduce(lista):
    for elemento in lista:
        elemento[1] = len(elemento[1])

print("Se pide el nombre del archivo de entrada, el cual contiene la letra de la canción.")
nombre_archivo_entrada = input("Ingrese el nombre del archivo con la letras: ")
print("Luego se pide el nombre del archivo en el cual va a estar el conteo de palabras.")
nombre_archivo_salida = input("Ingrese el nombre del archivo de salida: ")

print("Se llama a la función Map, pasando como argumento el nombre del archivo de entrada, para al final retornar una lista.")
lista = Map(nombre_archivo_entrada)
print("La función Map retorna esto: \n\n", lista, "\n")

print("Luego se llama la función ShuffleSort, pasando como argumento la lista obtenida anteriormente, retornando la lista cambiada.")
lista = ShuffleSort(lista)
print("La función ShuffleSort retorna esto: \n\n", lista, "\n")

print("Finalmente se llama la función Reduce, pasando como argumento la lista para así modificar a la misma.")
Reduce(lista)
print("La función Reduce modifica la lista dejandola así: \n\n", lista, "\n")

print("Finalmente se abre/crea un archivo con el nombre especificado anteriormente para almacenar la cantidad de repeticiones de cada palabra.")
archivo_salida = open(nombre_archivo_salida, "w")

for palabra in lista:
    archivo_salida.write("{} {}\n".format(palabra[0], palabra[1]))

archivo_salida.close()
