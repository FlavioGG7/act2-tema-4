"""programa que lea una matriz de 3x3,  la almacene en una lista de listas y calcule su transpuesta (intercambiar filas por columnas)"""
FILAS = 3
COLUMNAS = 3


def main():
    pass


def leer_entero(mensaje):
    """Pide un número entero y repite la solicitud hasta que sea válido."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Entrada no válida. Debes ingresar un número entero.")


def leer_matriz():
    """Lee una matriz de FILAS x COLUMNAS desde el teclado y la devuelve
    como lista de listas."""
    matriz = []

    for i in range(FILAS):
        fila = []
        for j in range(COLUMNAS):
            mensaje = f"Elemento [{i + 1}][{j + 1}]: "
            fila.append(leer_entero(mensaje))
        matriz.append(fila)

    return matriz


def transponer(matriz):
    """Devuelve la transpuesta de la matriz: el elemento [i][j] de la
    original pasa a ser el elemento [j][i] de la transpuesta."""
    transpuesta = []

    # Ahora se recorre por columnas: cada columna original será una fila
    for j in range(COLUMNAS):
        fila = []
        for i in range(FILAS):
            fila.append(matriz[i][j])
        transpuesta.append(fila)

    return transpuesta


def mostrar_matriz(titulo, matriz):
    """Imprime una matriz fila por fila con un título."""
    print(f"\n{titulo}:")
    for fila in matriz:
        print(" ".join(f"{numero:5}" for numero in fila))


def main():
    print("Ingresa los elementos de la matriz de 3x3:")
    matriz = leer_matriz()

    transpuesta = transponer(matriz)

    mostrar_matriz("Matriz original", matriz)
    mostrar_matriz("Matriz transpuesta", transpuesta)


if __name__ == "__main__":
    main()