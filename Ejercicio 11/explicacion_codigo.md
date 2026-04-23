# Explicación sencilla del código (Flask + Scanner QR)

Este código crea una aplicación web básica usando **Flask**, que
permite:

-   Iniciar sesión con usuario y contraseña
-   Escanear códigos QR desde la cámara
-   Mostrar los resultados en pantalla
-   Detectar si el QR contiene datos de WiFi

------------------------------------------------------------------------

## 1. Importaciones

``` python
from flask import Flask, render_template_string, request, redirect, session, jsonify
```

Aquí se importan herramientas de Flask:

-   `Flask`: crea la aplicación
-   `render_template_string`: permite usar HTML dentro del código
-   `request`: obtiene datos enviados desde formularios
-   `redirect`: redirige a otra página
-   `session`: guarda datos del usuario (como si inició sesión)
-   `jsonify`: devuelve respuestas en formato JSON

------------------------------------------------------------------------

## 2. Configuración básica

``` python
app = Flask(__name__)
app.secret_key = "seguridad_basica_2026"
```

-   Se crea la aplicación
-   `secret_key` sirve para proteger la sesión

------------------------------------------------------------------------

## 3. Credenciales

``` python
CREDENCIALES = {"usuario": "admin", "clave": "admin2026"}
```

Se define un usuario y contraseña simples para entrar.

------------------------------------------------------------------------

## 4. HTML dentro del código

Aquí se define toda la página web como texto.

Tiene dos partes:

### 🔹 Login

Si el usuario NO ha iniciado sesión: - Se muestra un formulario con
usuario y contraseña

### 🔹 Scanner

Si ya inició sesión: - Se activa la cámara - Se escanean códigos QR - Se
muestran resultados

------------------------------------------------------------------------

## 5. JavaScript (scanner QR)

``` javascript
function onScanSuccess(decodedText)
```

Cuando se escanea un código:

-   Se muestra el resultado en pantalla
-   Se detecta si es formato WiFi (`WIFI:`)
-   Si es WiFi:
    -   Extrae nombre de red (SSID)
    -   Extrae contraseña
-   Si no:
    -   Solo muestra el texto

También envía el dato al servidor con `fetch`

------------------------------------------------------------------------

## 6. Rutas de Flask

### Ruta principal `/`

``` python
@app.route("/", methods=["GET", "POST"])
```

-   Si es GET → muestra la página
-   Si es POST → valida usuario y contraseña

Si son correctos: - Guarda sesión - Redirige

------------------------------------------------------------------------

### Ruta `/registro`

``` python
@app.route("/registro", methods=["POST"])
```

-   Recibe datos del QR
-   Los imprime en la consola

------------------------------------------------------------------------

### Ruta `/salir`

``` python
@app.route("/salir")
```

-   Cierra la sesión
-   Regresa al inicio

------------------------------------------------------------------------

## 7. Ejecutar la app

``` python
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, ssl_context='adhoc')
```

-   Ejecuta el servidor
-   Usa HTTPS (`ssl_context='adhoc'`) para permitir usar la cámara

------------------------------------------------------------------------

## 🧠 En resumen

Este programa:

1.  Protege el acceso con login
2.  Usa la cámara para escanear QR
3.  Muestra resultados en pantalla
4.  Detecta datos especiales como WiFi
5.  Guarda registros en el servidor

------------------------------------------------------------------------

## ⚠️ Nota importante

Este sistema es **muy básico**: - Las credenciales están en el código -
No hay base de datos - No es seguro para producción

Sirve para aprender o proyectos escolares 👍
