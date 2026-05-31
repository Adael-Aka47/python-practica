# Repetir hasta que el usuario escriba "salir"

while True:
    dato = input("Escribe algo (o 'salir' para terminar): ")

    if dato == "salir":
        print("Programa terminado")
        break

    print("Escribiste:", dato)
