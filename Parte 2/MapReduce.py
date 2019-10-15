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

bandera = True
nombre_archivo_entrada = input("Ingrese el nombre del archivo con la letras: ")
lista = Map(nombre_archivo_entrada)
while bandera:
    nombre_archivo_entrada = input("Ingrese el nombre del archivo con la letras: ")
    if nombre_archivo_entrada == "q":
        bandera = False
    else:
        lista.extend(Map(nombre_archivo_entrada))

nombre_archivo_salida = input("Ingrese el nombre del archivo de salida: ")

lista = ShuffleSort(lista)
print(lista)
Reduce(lista)

archivo_salida = open(nombre_archivo_salida, "w")

for palabra in lista:
    archivo_salida.write("{} {}\n".format(palabra[0], palabra[1]))

archivo_salida.close()
