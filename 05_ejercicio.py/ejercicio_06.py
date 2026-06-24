#Enunciado: Un supermercado aplica descuentos especiales a sus clientes. Para acceder al descuento, el cliente debe ser mayor #de 60 años o tener una tarjeta de socio, y además el total de su compra debe superar los $10.000.

#Indicaciones paso a paso:

#Solicita al usuario su edad, si tiene tarjeta de socio (sí/no) y el monto total de su compra.
#Verifica si cumple las condiciones: el monto debe superar $10.000 y debe ser mayor de 60 años o tener tarjeta de socio.
#Muestra un mensaje indicando si obtiene el descuento del 15% o si no califica, mostrando el monto final en cada caso.
#Puntos asignados: 20 pts

#Criterios evaluados:

#Uso correcto de operadores lógicos (10 pts)
#Validación de condiciones y entrada de datos (5 pts)
#Claridad de la salida (5 pts)

edad = int(input("Ingresa tu edad: "))
socio = input("Tienes tarjeta de socio (S/N)").lower()
total = int(input("Ingresa el monto total: "))

descuento = total*15/100 
total_1 = total-descuento
if total >= 10000 and (socio == "s" or edad >= 65 ):
    print(f"Obtienes un descuento del 15% el total es $:{total_1}")
else:
    print(f"No obtienes descuento el total es: {total} ")

