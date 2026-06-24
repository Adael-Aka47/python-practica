#Problema 2: Registro de Ventas de una Tienda (35 pts)
#Enunciado: Una pequeña tienda registra las ventas diarias de 3 vendedores durante 3 días de la semana. El dueño quiere #saber el rendimiento de cada vendedor y si alguno tuvo bajo desempeño.

#Indicaciones paso a paso:

#Crea una matriz 3x3 para guardar los montos de ventas (cada fila es un vendedor, cada columna es un día).
#Calcula el total de ventas de cada vendedor (suma por fila solamente).
#Identifica qué vendedor tuvo el mayor total de ventas.
#Muestra una alerta si el total de algún vendedor es menor a $30.000.
#Puntos asignados: 35 pts

#Criterios evaluados:

#Representación correcta de la matriz (10 pts)
#Cálculo correcto del total por vendedor (10 pts)
#Identificación del mejor vendedor (10 pts)
#Claridad en mensajes y formato (5 pts)


ventas = [
    [15000, 20000, 10000], #vendedor 1
    [15000, 20000, 15000], #vendedor 2
    [15000, 20000, 25000]  #vendedor 3
]
vendedor1 = ventas[0]
vendedor2 = ventas[1]
vendedor3 = ventas[2]
total_1 = sum(vendedor1)
total_2 = sum(vendedor2)
total_3 = sum(vendedor3)
print(f"Vendedor 1: Total ventas = {total_1}")
print(f"Vendedor 2: Total ventas = {total_2}")
print(f"Vendedor 3: Total ventas = {total_3}")
if total_1 > total_2 and total_1 > total_3:
   print(f"Es el mejor vendedor este mes con: {total_1}")
elif total_2 > total_1 and total_2 > total_3:
    print(f"Es el mejor vendedor este mes con: {total_2}")
else: 
    print(f"Es el mejor vendedor este mes con: {total_3}")








       
        
             