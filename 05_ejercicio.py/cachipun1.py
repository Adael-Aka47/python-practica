import random

opciones = ["piedra", "papel", "tijeras"]

def comprobar_ganador(jugador, cpu):
    if (
        (jugador == "piedra" and cpu == "tijeras") or
        (jugador == "papel" and cpu == "piedra") or
        (jugador == "")
    
        )