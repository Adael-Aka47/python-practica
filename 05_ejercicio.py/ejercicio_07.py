#Ejercicio: Control de Acceso a Evento
#Crear un programa que:
#Pida al usuario:
#Edad
#Si tiene entrada (si/no)
#Si está en lista VIP (si/no)
#El sistema debe permitir entrada SOLO si:
#Tiene 18 años o más
#Y además:
#Tiene entrada o está en lista VIP
#Mostrar:
# "Acceso permitido"
# "Acceso denegado"
# "Eres menor de edad"

edad = int(input("Ingresa tu edad: "))
entrada = input("Tienes entrada (S/N) ").lower()
vip = input("Eres cliente VIP (S/N)").lower()

if edad >= 18 and (entrada == "s" or vip == "s"):
    print("Puedes ingresar.")
elif edad < 18:
    print("Eres menor de edad, acceso denegado ")
else: 
    print("Acceso denegado.")
