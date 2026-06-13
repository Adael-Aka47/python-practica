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

# Desarrolla el código a continuación:



while True:
        while True:
            try:
                edad = int(input("¿Hola bienvenido, qué edad tienes?"))
                break
            except ValueError:
                  print("número incorrecto")
        while True:
            try: 
                membrecia = input("Ingresa si tienes membrecia o no (si y no)").lower
                break
            except ValueError:
                print("No ingresaste bien los datos")
        while True:
             try:
                  codigo = input("Ingresa si tienes código de invitado (si y no)")
                  break
             except ValueError:
                  print("No ingresaste bien los datos")
            if  (edad >= 18 and membrecia == "si" and codigo == "si"):
             print("Puedes ingresar, todos tus datos son correctos.")
            elif (edad != 18 and membrecia != "si" and codigo != "si"):
             print("No puedes ingresar, no cumples con nada ")
        
             