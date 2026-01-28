def convertidor():
    try:
        print("Hola Bienvenido")

        celcius = float(input("Ingresa Grados Celcius: "))
        fahrenheit = (celcius * 9/5) + 32

        print(f"la conversion de celcius a fahrenheit es: {fahrenheit}")
    except ValueError:
        print("Algo salio mal, intenta de nuevo :(")

loop =  True

while loop:
    try:
        print("-----Convertidor de Celcius a Fahrenheit-----")
        opcion = int(input("(Menu)\nCovertir - (1)\nSalir - (0)\n"))
        if opcion == 0:
            break
        elif opcion == 1:
            convertidor()
        else:
            print("Esa no es una opcion, vuelve a intentar...")
    except ValueError:
        print("Esa no es una opcion, vuelve a intentar...")