# Explicación sencilla del funcionamiento del programa

## 📥 Entrada del número

El programa empieza pidiéndole al usuario un número y lo guarda. Como lo
que se escribe normalmente se interpreta como texto, primero lo
transforma a valor numérico para poder hacer cálculos sin errores.

------------------------------------------------------------------------

## 🔁 Idea general del proceso

Para convertir el número a distintos sistemas, el programa trabaja con
una copia del valor original. Así puede modificar esa copia paso a paso
sin alterar el dato inicial.\
También crea espacios vacíos donde se irá armando cada resultado.

------------------------------------------------------------------------

## ⚙️ Cómo se hace la conversión

El método que usa es repetir un mismo procedimiento:

1.  Mientras el número sea mayor que cero:
    -   Se divide entre la base que se quiere usar.
    -   Se obtiene el sobrante de esa división.
    -   Ese sobrante se vuelve un dígito del resultado.
2.  El número se reduce usando la división entera.
3.  El proceso se repite hasta que el número llega a cero.

Los dígitos se van colocando en orden correcto para formar el resultado
final.

------------------------------------------------------------------------

## 🔢 Sistemas a los que se convierte

El programa aplica esa misma lógica varias veces, cambiando únicamente
la base numérica:

-   Base 2 → Binario\
-   Base 8 → Octal\
-   Base 16 → Hexadecimal

En el caso hexadecimal hay un detalle especial: algunos valores no se
escriben con números normales, sino con letras. El programa reemplaza
esos valores automáticamente para que el resultado sea correcto.

------------------------------------------------------------------------

## ✅ Resultado final

Al terminar cada conversión, el programa muestra el número ya
transformado en el sistema correspondiente. Así se obtiene el mismo
valor representado de distintas maneras.
