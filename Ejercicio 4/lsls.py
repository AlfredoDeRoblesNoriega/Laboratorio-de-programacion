uservalido = "admin"
contrasenavalida = "Admin2026"

intentos = 0
logincorrecto = False
while intentos < 3:

    user = input("Escribe el usuario: ")
    contra = input("Escribe la contraseña: ")

    if user == "":
     print("Error no debe estar vacío")
     intentos += 1

    if " " in user:
       print("Error no debe tener espacios.")
       intentos += 1

    if len(contra) < 8:
        print("Error, al menos 8 caracteres.")
        intentos += 1

    letra_correcta = False
    numero_correcto = False
    for c in contra:
     codigo = ord(c)
     if (65 <= codigo <= 90) or (97 <= codigo <= 122):
        letra_correcta = True

     if 48 <= codigo <= 57:
            numero_correcto = True

    if not letra_correcta or not numero_correcto:
            print("Error al menos una letra y numero.")
            intentos +=1

    if user == uservalido and contra == contrasenavalida:
        print("Bienvenid@.")
        logincorrecto = True
        
    elif user != uservalido or contra != contrasenavalida:
        print("Error, datos invalidos.")
        intentos += 1

    if intentos == 3:
     print("Llegaste al máximo de intentos.")
     break 

    while logincorrecto == True:
     print("1. Clasificar número")
     print("2. Categoría de edad y permisos")
     print("3. Calcular tarifa final")
     print("4. Cerrar sesión")
     print("5. Salir")
     seleccion = input("Selecciona una opción: ")

     if seleccion == "1":
         numero = int(input("Escribe un número: "))
         type(numero) == int
         if numero == 0:
             print("El número es cero.")
         elif numero > 0:
             print("El número es positivo.")
         elif numero < 0:
             print("El número es negativo.") 
         if numero %2 == 0:
             print("El número es par.")
         elif numero == 0:
             print("El 0 no es par ni impar.")
         else:
             print("El número es impar") 

     elif seleccion == "2":
         edad = int(input("Escribe tu edad: "))
         type(edad) == int
         id_oficial = str(input("¿Cuenta con identificación oficial? (S/N): "))
         licencia = str(input("¿Cuenta con licencia para conducir? (S/N): "))
         if edad < 0 or edad > 120:
             print("Edad inválida.")
         if 0 <= edad <= 12:
             print("niñez.")
         elif 13 <= edad <=17:
             print("adolescencia.")
         elif 18 <= edad <= 64:
             print("adultes.")
         else:
             print("adulto mayor.")
         if edad >= 13:
             print("Puedes registrarte.")
         elif edad >= 18:
             print("Puedes comprar sin tutor.")
         else: 
             print("Requieres un tutor.") 
         if edad >= 18 and licencia == "S":
             print("Puedes conducir.")
         else:
             print("No puedes conducir.")
         if edad >= 21 and id_oficial == "S":
             print("Tienes acceso al servicio premium.")
         else: 
             print("No tienes acceso .")

 
     elif seleccion == "3":
         print("Calculando la tarifa final...")

     elif seleccion == "4":
         print("Cerrando sesión...")
         break
     elif seleccion == "5":
         break
    break