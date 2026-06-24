# Actividad
# Tomando este codigo como base:
# Desarrollen las siguientes modificaciones a su codigo:
# 1.- Mostrar con SCORE con las estadisticas de cada juego para ver quien va ganando
# 2.- Crear un bucle y que para terminar de jugar escriban "salir"
# 3.- Que el usuario no pueda ingresar otras alternativas que no estén en las opciones
# 4.- Añadan otra opcion al piedra, papel y tijeras, obviamente que haya una logica detras
# 5.- Transformar con el input todo el texto introducido por el usuario a minusculas.


import random
opciones = ["piedra", "papel", "tijeras"]

def comprobar_ganador(jugador, cpu):
    if (
    (jugador == "piedra" and cpu == "tijeras") or 
    (jugador == "papel" and cpu == "piedra") or 
    (jugador == "tijeras" and cpu == "papel")
    ):
        return True
    return False
player = input("Ingresa tu opción (o Salir para terminar): ").lower()
while True:
    if player == "salir":
        print("Has salido del juego.")
    if player != "piedra" or "tijeras" or "papel" or "salir":
        print("Elección no valida.")
    break
computer = random.choice(opciones)
print(f"La Computadora saco: {computer}")
if player == computer:
    print("Empate")
elif comprobar_ganador(player,computer):
    print(f"Ganaste porque la CPU escogió: {computer}")
else:
    print("Perdiste")  