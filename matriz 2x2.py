"""programa que lea dos matrices de 2×2 (4 números cada una), las almacene en listas de listas y calcule la suma de ambas matrices"""
def main():
    matriz1 = []
    matriz2 = []
    print("Ingrese los elementos de la primera matriz (2x2):")
    for i in range(2):
        fila = []
        for j in range(2):
            numero = int(input(f"Ingrese el número entero para la posición ({i+1},{j+1}): "))
            fila.append(numero)
        matriz1.append(fila)

    print("Ingrese los elementos de la segunda matriz (2x2):")
    for i in range(2):
        fila = []
        for j in range(2):
            numero = int(input(f"Ingrese el número entero para la posición ({i+1},{j+1}): "))
            fila.append(numero)
        matriz2.append(fila)

    # Calcular la suma de las matrices
    matriz_suma = []
    for i in range(2):
        fila_suma = []
        for j in range(2):
            suma = matriz1[i][j] + matriz2[i][j]
            fila_suma.append(suma)
        matriz_suma.append(fila_suma)

    print("Matriz 1:")
    for fila in matriz1:
        print(fila)

    print("Matriz 2:")
    for fila in matriz2:
        print(fila)

    print("Suma de las matrices:")
    for fila in matriz_suma:
        print(fila)

if __name__ == "__main__":
    main()