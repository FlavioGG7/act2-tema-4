"""programa que lea 6 numeros enteros, los almacene en una lista y posteriormente invierta el orden de los elementos."""
def main():
    numeros = []
    for i in range(6):
        numero = int(input(f"Ingrese el número entero {len(numeros) + 1} de 6: "))
        numeros.append(numero)
    
    print("Lista original:", numeros)
    
    numeros_invertidos = numeros[::-1]   # se usa ::-1 para invertir la lista
    print("Lista invertida:", numeros_invertidos)

if __name__ == "__main__":
    main()
    