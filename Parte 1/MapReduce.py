def Map(nombre_archivo):
    archivo_letra = open(nombre_archivo)
    lista = []
    
    for linea in archivo_letra:
        if linea != "\n":
            linea = linea.strip().split()
            for elemento in linea:
                lista.append((elemento.lower(), 1))
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

def Reduce():
    pass

nombre_archivo = input("Ingrese el nombre del archivo: ")

lista = Map(nombre_archivo)

lista = ShuffleSort(lista)

