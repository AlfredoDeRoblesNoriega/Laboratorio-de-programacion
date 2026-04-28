from flask import Flask, render_template_string, request, redirect, session, jsonify

app = Flask(__name__)
app.secret_key = "seguridad_basica_2026"

CREDENCIALES = {"usuario": "admin", "clave": "admin2026"}

HTML_BASE = """
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Punto de Venta</title>
<script src="https://unpkg.com/html5-qrcode"></script>

<style>
body {
    margin: 0;
    font-family: Arial;
    background: #eef1f5;
}

/* HEADER tipo Walmart */
header {
    background: #0071ce;
    color: white;
    padding: 15px;
    font-size: 22px;
    text-align: center;
}

/* CONTENEDOR */
.container {
    max-width: 900px;
    margin: auto;
    padding: 20px;
}

/* BOTONES */
.btn {
    width: 100%;
    padding: 14px;
    margin-bottom: 10px;
    background: #0071ce;
    color: white;
    border: none;
    border-radius: 6px;
    font-size: 16px;
    cursor: pointer;
}

.btn:hover {
    background: #005fa3;
}

/* LISTA PRODUCTOS */
.productos {
    background: white;
    border-radius: 10px;
    padding: 15px;
}

.producto {
    display: flex;
    justify-content: space-between;
    padding: 12px;
    border-bottom: 1px solid #ddd;
}

/* TOTAL */
.total {
    margin-top: 15px;
    font-size: 18px;
    font-weight: bold;
}

/* MODAL SCANNER */
.modal {
    display: none;
    position: fixed;
    z-index: 100;
    width: 100%;
    height: 100%;
    background: rgba(0,0,0,0.7);
    top: 0;
}

.modal-content {
    background: white;
    margin: 10% auto;
    padding: 20px;
    width: 90%;
    max-width: 400px;
    border-radius: 10px;
    text-align: center;
}

.close {
    float: right;
    cursor: pointer;
    font-size: 20px;
}

#reader {
    width: 100%;
}
</style>
</head>

<body>

<header>🛒 Punto de Venta</header>

<div class="container">

{% if not session.get('auth') %}

<h2>Login</h2>
<form method="POST">
<input type="text" name="u" placeholder="Usuario" required>
<input type="password" name="p" placeholder="Contraseña" required>
<button class="btn">Entrar</button>
</form>

{% else %}

<!-- PANTALLA PRINCIPAL -->
<button class="btn" onclick="abrirScanner()">📷 Escanear producto</button>
<button class="btn" onclick="limpiar()">🗑 Vaciar carrito</button>

<div class="productos">
<h3>Productos</h3>
<div id="lista"></div>
<div class="total">Total: $<span id="total">0</span></div>
</div>

<p><a href="/salir">Cerrar sesión</a></p>

{% endif %}

</div>

<!-- PANTALLA 2: SCANNER -->
<div id="modal" class="modal">
<div class="modal-content">
<span class="close" onclick="cerrarScanner()">✖</span>
<h3>Escanear código</h3>
<div id="reader"></div>
</div>
</div>

<script>

let scanner;
let activo = false;
let total = 0;

/* PRECIOS SIMULADOS */
function precioRandom(){
    return Math.floor(Math.random()*100)+10;
}

/* ABRIR SCANNER */
function abrirScanner(){
    document.getElementById("modal").style.display = "block";

    if(!activo){
        scanner = new Html5QrcodeScanner("reader", {
            fps: 10,
            qrbox: 200
        });

        scanner.render(procesar);
        activo = true;
    }
}

/* CERRAR SCANNER */
function cerrarScanner(){
    document.getElementById("modal").style.display = "none";
}

/* PROCESAR PRODUCTO */
function procesar(codigo){

    let precio = precioRandom();
    total += precio;

    let lista = document.getElementById("lista");

    let item = document.createElement("div");
    item.className = "producto";

    item.innerHTML = `
        <span>${codigo} - $${precio}</span>
        <button onclick="eliminar(this, ${precio})">❌</button>
    `;

    lista.prepend(item);

    document.getElementById("total").innerText = total;

    fetch('/registro', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({dato: codigo, precio: precio})
    });

    cerrarScanner();
}

/* ELIMINAR PRODUCTO */
function eliminar(btn, precio){
    btn.parentElement.remove();
    total -= precio;
    document.getElementById("total").innerText = total;
}

/* LIMPIAR TODO */
function limpiar(){
    document.getElementById("lista").innerHTML = "";
    total = 0;
    document.getElementById("total").innerText = total;
}

</script>

</body>
</html>
"""

@app.route("/", methods=["GET","POST"])
def principal():
    error = None
    if request.method == "POST":
        u = request.form.get("u")
        p = request.form.get("p")
        if u == CREDENCIALES["usuario"] and p == CREDENCIALES["clave"]:
            session["auth"] = True
            return redirect("/")
        error = "Error de acceso"
    return render_template_string(HTML_BASE, e=error)

@app.route("/registro", methods=["POST"])
def registro():
    data = request.json
    print("Producto:", data)
    return jsonify({"ok": True})

@app.route("/salir")
def salir():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0", port=5000, ssl_context='adhoc')