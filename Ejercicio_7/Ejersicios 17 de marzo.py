def e1():
      print("Ejercicio 1 repetir palabra")
      texto_ingresado = str(input("Escriba alguna palabra: "))
      for vuelta in range(10):
            print(texto_ingresado)


def e2(): 
      print("Ejercicio 2 Años cumplidos")     
      edad_actual = int(input("¿Cuantos años tienes? "))
      for conteo in range(edad_actual):
            print("Feliz cumpleaños, ten un buen dia:)", edad_actual)

def e3():
      print("Ejercicio 3 numeros impares hasta donde tu quieras")
      numero_limite = int(input("Escriba un numero: "))
      for valor in range(numero_limite):
            if valor % 2 != 0:
                  print(valor)

def e4():
      print("Ejercicio 4 cuenta hacia atras")
      numero_inicio = int(input("Escribe un numero: "))
      for conteo in range(numero_inicio, 0, -1):
            print(conteo ,",")

def e5():
      print("calculadora de inversion, interes anual, numeros de años y capital obtenido")
      monto = float(input("¿Cuanto dinero quiere invertir? "))
      porcentaje = float(input("¿Cual es el interes anual? "))
      tiempo = int(input("¿Cuantos años desea invertir? "))
      for ciclo in range(tiempo):
            monto = monto + (monto * (porcentaje / 100))
      print(f"El capital obtenido después de {tiempo} años es: {monto:.2f}")

def e6():
      print("Ejercicio 6 triangulo de asteriscos")
      limite = int(input("Escriba un numero: "))
      for nivel in range(1, limite + 1):
            print("*" * nivel)

def e7():
      print("Ejercicio 7 tabla de multiplicar del 1 al 10")
      for base in range(1, 11):
               print(f"Tabla del {base}:")
               for factor in range(1, 11):
                     print(f"{base} x {factor} = {base * factor}")
               print()           

def e8():
     print("Ejercicio 8: Triángulo de números impares")

     total = int(input("Escriba un número entero: "))

     for fila in range(1, total + 1):
    
          limite_impar = 2 * fila - 1
    
          for numero in range(limite_impar, 0, -2):
           print(numero, end=" ")
           print()  


def e9():
      print("Ejercicio 9: La contraseña")
      print("Escribe una contraseña")
      clave_guardada = str(input("Contraseña:  "))

      while True:
            print("¿Cuál es la contraseña?")
            clave_intento = str(input("Contraseña:  "))
            if clave_guardada == clave_intento:
                  print("Contraseña correcta")
                  break
            else:
                  print("Contraseña incorrecta")

      
def e10():
      print("Ejercicio 10: Primo o no primo")
      valor_usuario = int(input("Escribe un número entero: "))
      if valor_usuario < 2:
            print(f"{valor_usuario} no es primo.")
      else:
            indicador = True
            for divisor in range(2, int(valor_usuario**0.5) + 1):
                  if valor_usuario % divisor == 0:
                        indicador = False
                        break
            if indicador:
                  print(f"{valor_usuario} es primo.")
            else:
                  print(f"{valor_usuario} no es primo.")


def e11():
      print("Ejercicio 11: descomponiendo la palabra")
      cadena = str(input("Escribe una palabra: "))
      for simbolo in cadena:
            print(simbolo)

   
def e12():
      print("Ejercicio 12: ¿Cuantas veces aparece la letra en la frase?")
      texto_completo = str(input("Escribe una frase: "))
      caracter_buscar = str(input("Escribe una letra: "))
      acumulador = 0
      for caracter in texto_completo:
            if caracter == caracter_buscar:
                  acumulador += 1
      print(f"La letra '{caracter_buscar}' aparece {acumulador} veces en la frase.")
     

def e13():
      print("Ejercicio 13: Eco hasta escribir 'salir'")
      while True:
         entrada = str(input("Escribe algo (o 'salir' para terminar): "))
         if entrada == "salir":
            print("nos vemos my pana")
            break
         else:
            print(entrada)


def main():
      while True:
            print("\n" + "="*40)
            print("MENU")
            print("="*40)
            print("1. Ejercicio 1 - Repetir palabra")
            print("2. Ejercicio 2 - Años cumplidos")
            print("3. Ejercicio 3 - Números impares")
            print("4. Ejercicio 4 - Cuenta hacia atrás")
            print("5. Ejercicio 5 - Calculadora de inversión")
            print("6. Ejercicio 6 - Triángulo de asteriscos")
            print("7. Ejercicio 7 - Tabla de multiplicar")
            print("8. Ejercicio 8 - Triángulo de números impares")
            print("9. Ejercicio 9 - La contraseña")
            print("10. Ejercicio 10 - Primo o no primo")
            print("11. Ejercicio 11 - Descomponiendo la palabra")
            print("12. Ejercicio 12 - Contar letra en frase")
            print("13. Ejercicio 13 - Eco hasta salir")
            print("0. Salir del programa")
            print("="*40)
            
            opcion_menu = input("Selecciona un ejercicio: ")
            
            match opcion_menu:
               case "1":
                  e1()
               case "2":
                  e2()
               case "3":
                  e3()
               case "4":
                  e4()
               case "5":
                  e5()
               case "6":
                  e6()
               case "7":
                  e7()
               case "8":
                  e8()
               case "9":
                  e9()
               case "10":
                  e10()
               case "11":
                  e11()
               case "12":
                  e12()
               case "13":
                  e13()
               case "0":
                  print("Good Bye"*70)
                  break
               case _:
                  print("Opción no válida. Intenta de nuevo.")
            
            input("\nClick en Enter para volver al menú...")


if __name__ == "__main__":
      main()