# Problema 1: Revisión de Stock en Bodega
#
# Una tienda tiene 5 productos y cada uno tiene una cantidad en stock.
# Debes realizar lo siguiente:
#
# 1. Crea una lista llamada 'stocks' con la cantidad de stock de cada producto (puedes usar los valores que desees).
# 2. Calcula la suma total de productos disponibles usando la función sum().
# 3. Verifica si todos los productos tienen más de 10 unidades:
#    - Usa un ciclo (for) y una condicional (if) para revisar cada elemento de la lista.
#    - Si algún producto tiene 10 o menos unidades, muestra un mensaje indicando cuál(es) producto(s) tienen bajo stock.
#    - Si todos tienen más de 10, muestra un mensaje indicando que el stock es suficiente.
#
# Escribe tu solución debajo de este comentario.


stocks = [9,20,20,20,20]

suma = sum(stocks)
print("La suma del Stock es",suma)

bajo_stock = False

for i, stock in enumerate(stocks, start=1):
    if stock < 10:
        print(f"Producto {i}: Tiene {stock} unidades.")
        bajo_stock = True
if not bajo_stock:
    print("Todos los productos estan abastecidos.")