# Ejercicio 3: Verificación de Usuario
# 
# Este programa verifica si un usuario puede acceder al sistema según las siguientes reglas:
# - Debe tener al menos 18 años.
# - Además, debe tener una membresía activa O un código de invitado.
#
# Instrucciones:
# 1. Usa la función input() para pedir al usuario:
#    - Su edad (como número entero).
#    - Si tiene membresía activa ('s' para sí, 'n' para no).
#    - Si tiene código de invitado ('s' para sí, 'n' para no).
# 2. Usa operadores lógicos (and, or) para verificar las condiciones.
# 3. Muestra un mensaje indicando si el acceso está permitido o denegado.

edad = int(input("Ingresa tu edad"))
membresia = input("Tienes mebresia (S/N)").lower()
codigo = input("Tienes un codigo de invitación (S/N)").lower()

if edad >= 18 and (membresia == "s" or codigo == "s"):
    print("Tu datos son correctos")
else:
    print("Tus datos no son correctos")
