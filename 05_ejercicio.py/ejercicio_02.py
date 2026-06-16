# Problema 2: Encuesta de Satisfacción
#
# Este programa permite ingresar las respuestas de una encuesta aplicada a 3 personas,
# con 3 preguntas cada una. Cada respuesta es un número del 1 al 5.
#
# El programa debe:
# 1. Mostrar todas las respuestas en formato de matriz 3x3.
# 2. Calcular y mostrar el promedio de respuestas por persona (por fila).
# 3. Calcular y mostrar el promedio de respuestas por pregunta (por columna).
# 4. Mostrar un mensaje si alguna persona tiene promedio menor a 3.
#
# ¡Ahora completa el código siguiendo estos pasos!

# Encuesta de Satisfacción

# Encuesta de satisfacción

matriz = []

# Ingreso de datos
for i in range(3):
    fila = [int(input(f"Persona {i+1}, pregunta {j+1}: ")) for j in range(3)]
    matriz.append(fila)

# Mostrar matriz
print("\nRespuestas:")
for fila in matriz:
    print(fila)

# Promedio por persona
print("\nPromedio por persona:")
for fila in matriz:
    prom = sum(fila) / len(fila)
    print(prom)
    if prom < 3:
        print("Baja satisfacción")

# Promedio por pregunta
print("\nPromedio por pregunta:")
for j in range(3):
    prom = sum(fila[j] for fila in matriz) / len(matriz)
    print(prom)