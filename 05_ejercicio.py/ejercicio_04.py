
#Problema 1: Control de Velocidad en una Autopista (25 pts)
#Enunciado: Una autopista instaló sensores para registrar la velocidad de los vehículos y detectar infracciones. Debes crear #un programa que analice los registros y emita alertas cuando corresponda.

#Indicaciones paso a paso:

#Solicita al usuario que ingrese 5 velocidades (en km/h).
#Guarda las velocidades en una lista.
#Calcula el promedio y la velocidad máxima registrada.
#Verifica si todas las velocidades están dentro del límite permitido (entre 60 y 120 km/h).
#Si alguna velocidad supera los 140 km/h o es menor a 20 km/h, muestra una advertencia de peligro.
#Puntos asignados: 25 pts

#Criterios evaluados:

#Uso correcto de lista y cálculos (10 pts)
#Evaluación de condiciones lógicas (10 pts)
#Orden y claridad del código (5 pts)
#
#Lista de Velocidades
vel = []
for i in range(1, 6):
    velocidad = int(input(f"Velocidad {i}: : "))
    #Despliega los datos ingresados de la variable ""velocidad""" en la Variable ""vel"""
    vel.append(velocidad)
    #Comparadores Logicos, if elif y else. 
    if velocidad < 20:
        print("Alerta, Velocidad bajo 20 Km/h80.")
    elif velocidad > 140:
        print(f"Alerta, velocidad sobre 140 Km/h.")
    else:
        print("Velocidad Normal.")
print("\nlista")
#Lista de Velocidades
for i, vel1 in enumerate(vel, start=1):
    print(f"velocidad {i}):{vel1}, Km/h")
max_vel = max(vel)
#Velocidad Máxima Ingresada
print(f"La velocidad máxima ingresada es: ", max_vel)
#Promedio y Suma
prom1 = sum(vel) / len(vel)
sum1 = sum(vel)
print(f"El promedio es: {prom1} \nLa suma es: {sum1}.")