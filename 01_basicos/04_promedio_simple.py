# Promedio Simple. 

suma = 0 
cantidad = int(input("Ingresa la cantidad de números a promediar: "))

for i in range(cantidad):
    suma = float(input("Ingresa las notas: "))
    suma += suma
    promedio = suma / cantidad

print("El promedio es",promedio)
