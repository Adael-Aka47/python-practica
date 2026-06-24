#Crea un programa que:

#Pida ingresar 5 notas (números entre 1 y 7).

#Por cada nota:
#Si es menor a 1 o mayor a 7 → mostrar "Nota inválida"
#Si está entre 1 y 7 → mostrar "Nota válida"

#Al final el programa debe:
# Mostrar el promedio de las notas válidas
# Mostrar la nota mayor
# Contar cuántas notas son reprobadas (menores a 4)

lista_notas = []
reprobadas = 0
for i in range(1, 6):
    while True:
        try:
            notas = int(input(f"Ingresa la nota Número {i}: "))
            if 1 <= notas <= 7:
                lista_notas.append(notas)
                if notas < 4:
                    reprobadas += 1
                print("Nota válida")
                break
            else:
                print("Nota inválida")
            
        except ValueError:
            print("Número Incorrecto.")

print("\nNotas Ingresadas")
for nota in lista_notas:
    print(nota)

if lista_notas:
    promedio = sum(lista_notas) / len(lista_notas)
    nota_max = max(lista_notas)
    print(f"Nota Máxima Ingresada = {nota_max}")
else:
    promedio = 0
    print("No se ingresaron notas válidas.")

print(f"Notas menor a 4 ingresadas: {reprobadas} \nPromedio de notas: {promedio}")
