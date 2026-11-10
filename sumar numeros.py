"""programa que lea 5 numeros enteros, los almacene en una lista y calcule la suma total de sus elementos"""
Cantidad_numeros = 5
def leer_numeros():
    numeros = []
    for i in range(Cantidad_numeros):
        while len (numeros) < Cantidad_numeros:
            try:
                numero = int(input(f"Ingrese el número {len(numeros) + 1} de {Cantidad_numeros}: "))
                numeros.append(numero)
            except ValueError:
                print("Por favor, ingrese un número entero válido.")
    return numeros
def calcular_suma(numeros):
    return sum(numeros)
def main():
    numeros = leer_numeros()
    suma_total = calcular_suma(numeros)
    print(f"La suma total de los números ingresados es: {suma_total}")

if __name__ == "__main__":
    main()