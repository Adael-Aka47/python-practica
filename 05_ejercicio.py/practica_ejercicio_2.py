matriz = []

for i in range(3):
    fila = [int(input(f"Persona {i+1}, pregunta {j+1} :")) for j in range(3)]
    matriz.append(fila)

print("\nRespuesta: ")
for fila in matriz:
    print(fila)


