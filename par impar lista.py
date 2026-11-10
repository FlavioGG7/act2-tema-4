"""Programa que lee 10 enteros, los almacena en una lista y cuenta
cuántos son pares y cuántos son impares."""

CANTIDAD_NUMEROS = 10


def leer_numeros(cantidad):
    """Lee `cantidad` números enteros desde el teclado y los devuelve
    en una lista. Si la entrada no es válida, vuelve a solicitarla."""
    numeros = []
    while len(numeros) < cantidad:
        entrada = input(f"Ingresa el número {len(numeros) + 1} de {cantidad}: ")
        try:
            numeros.append(int(entrada))
        except ValueError:
            print("Entrada no válida. Debes ingresar un número entero.")
    return numeros


def contar_pares_impares(numeros):
    """Devuelve una tupla (pares, impares) con la cantidad de cada tipo."""
    pares = sum(1 for numero in numeros if numero % 2 == 0)
    impares = len(numeros) - pares
    return pares, impares


def main():
    """Función principal del programa."""
    numeros = leer_numeros(CANTIDAD_NUMEROS)
    pares, impares = contar_pares_impares(numeros)

    print(f"\nLista de números: {numeros}")
    print(f"Cantidad de números pares: {pares}")
    print(f"Cantidad de números impares: {impares}")


if __name__ == "__main__":
    main()