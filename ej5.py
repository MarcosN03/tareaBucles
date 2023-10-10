def numero(inversion, intanual, numa):
    for i in range(1, numa + 1):
        print(inversion*intanual)
inversion = int(input("Introduce la cantidad a invertir:"))
intanual = int(input("Introduce el interés anual:"))
numa = int (input("Introduce el numero de años:"))
numero(inversion, intanual, numa)
