# Crear Entorno Virtual en Python con VS Code

> Guía paso a paso


---

## Paso 1 — Abrir carpeta del proyecto
Abre **Visual Studio Code** → `File > Open Folder` y selecciona tu carpeta.

![Paso 1](assets/imagen_paso1.png)

---

## Paso 2 — Abrir terminal integrada
Menú:
```
Terminal > New Terminal
```
Esto abre la consola dentro del proyecto.

![Paso 2](assets/imagen_paso2.png)

---

## Paso 3 — Crear entorno virtual
Comando:

```bash
python -m venv venv
```

**Qué hace:**
- `python -m venv` → crea entornos virtuales
- `venv` → nombre del entorno

Resultado: se crea carpeta `venv/`.

---

## Paso 4 — Activar entorno

### Windows
```bash
venv\Scripts\activate
```

### Mac/Linux
```bash
source venv/bin/activate
```

Si funciona verás:

```
(venv) ruta/proyecto>
```

![Paso 4](assets/imagen_paso3.png)

---

## Paso 5 — Seleccionar intérprete en VS Code
Presiona:

```
Ctrl + Shift + P
```

Escribe:

```
Python: Select Interpreter
```

Selecciona el que diga `venv`.

---

## Paso 6 — Instalar paquetes
Ejemplo instalar **numpy**

```bash
pip install numpy
```

**Qué hace:**  
Instala la librería dentro del entorno virtual (no global).

---

## Paso 7 — Verificar instalación
```bash
pip list
```

Muestra todas las librerías instaladas.

---

## Paso 8 — Desactivar entorno
```bash
deactivate
```

---

# Estructura final esperada

```
proyecto/
 ├── venv/
 ├── main.py
 └── README.md
```

---

# Explicación Conceptual

Un entorno virtual es un **aislador de dependencias**.

Permite:
- usar versiones distintas de librerías
- evitar conflictos
- mantener proyectos independientes

---

# Problemas comunes

### Error: python no reconocido
Solución → instalar Python y marcar **Add to PATH**

---

### Error: pip no funciona
Ejecutar:

```bash
python -m ensurepip --upgrade
```

---

# Buenas prácticas

✔ No subir carpeta `venv/` a GitHub  
✔ Añadir a `.gitignore`

```
venv/
```

---

# Fin
