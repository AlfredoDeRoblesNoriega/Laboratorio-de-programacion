# Código de Login en Python

``` python
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
```
