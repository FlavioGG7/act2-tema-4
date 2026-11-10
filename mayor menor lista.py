"""programa que lea 8 numeros, los almacene en una lista y determine cuál es el número mayor y cuál es el número menor."""
Cantidad_numeros = 8
def leer_numeros():
    numeros = []
    for i in range(Cantidad_numeros):
        while len(numeros) < Cantidad_numeros:
            try:
                numero = int(input(f"Ingrese el número {len(numeros) + 1} de {Cantidad_numeros}: "))
                numeros.append(numero)
            except ValueError:
                print("Por favor, ingrese un número entero válido.")
    return numeros

def encontrar_mayor_menor(numeros):
    return max(numeros), min(numeros)

def main():
    numeros = leer_numeros()
    mayor, menor = encontrar_mayor_menor(numeros)
    print(f"El número mayor es: {mayor}")
    print(f"El número menor es: {menor}")

if __name__ == "__main__":
    main()