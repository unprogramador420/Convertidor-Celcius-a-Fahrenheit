🌡️ Convertidor de Celsius a Fahrenheit en Python
Este es un programa sencillo e interactivo desarrollado en Python que permite realizar conversiones de temperatura. El proyecto destaca por el uso de estructuras de control y manejo de excepciones para garantizar que el programa no se detenga ante entradas inválidas.

🚀 FuncionalidadesInterfaz de Consola: Menú interactivo para elegir entre convertir grados o salir del programa.Conversión Precisa: Utiliza la fórmula estándar $F = (C \times 9/5) + 32$.Manejo de Errores: Implementa bloques try-except para capturar errores de entrada (como cuando el usuario ingresa letras en lugar de números).Bucle Continuo: El programa se mantiene activo hasta que el usuario decide finalizarlo explícitamente.

🛠️ Cómo funciona el código
La función convertidor():
Solicita la entrada de grados Celsius.
Realiza el cálculo matemático.
Si el usuario ingresa algo que no sea un número, el bloque except evita que el programa falle y muestra un mensaje amigable.
El Bucle Principal (while):
Controla el menú del programa.
Valida que la opción seleccionada sea un número entero (1 o 0).

💻 Ejemplo de Uso
-----Convertidor de Celcius a Fahrenheit-----
(Menu)
Covertir - (1)
Salir - (0)
1
Hola Bienvenido
Ingresa Grados Celcius: 25
la conversion de celcius a fahrenheit es: 77.0

📝 Requisitos
Python 3.x
