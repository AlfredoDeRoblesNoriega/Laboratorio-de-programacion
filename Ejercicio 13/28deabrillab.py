from flask import Flask, render_template_string, request, jsonify
import sqlite3

app = Flask(__name__)
app.secret_key = "admin2026"

# ==========================
# DB
# ==========================
def db():
    conn = sqlite3.connect("productos.db")
    conn.row_factory = sqlite3.Row
    return conn

def init():
    c = db()
    c.execute("""
    CREATE TABLE IF NOT EXISTS productos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        proveedor TEXT,
        nombre TEXT,
        codigo TEXT,
        cantidad INTEGER
    )
    """)
    c.commit()
    c.close()

init()

# ==========================
# INVENTARIO GLOBAL
# ==========================
inventario = {}

mock = {
    "123": {"nombre":"Cereal"},
    "456": {"nombre":"Leche"},
}

# ==========================
# BASE HTML
# ==========================
BASE = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Mineshop</title>
<script src="https://unpkg.com/html5-qrcode"></script>

<style>
body {margin:0;font-family:Segoe UI;background:#f1f5f9;}
.nav {
    background:#2563eb;
    color:white;
    padding:15px;
    display:flex;
    justify-content:space-between;
}
.nav a {color:white;margin:0 10px;text-decoration:none;font-weight:bold;}
.container {padding:20px;}
.card {
    background:white;
    padding:20px;
    border-radius:12px;
    box-shadow:0 4px 10px rgba(0,0,0,0.08);
    margin-bottom:20px;
}
button {
    background:#2563eb;color:white;border:none;
    padding:10px;border-radius:8px;cursor:pointer;margin:5px;
}
button:hover {background:#1d4ed8;}
table {width:100%;border-collapse:collapse;}
td,th {padding:10px;border-bottom:1px solid #ddd;}
.ok {color:green;font-weight:bold;}
</style>
</head>
<body>

<div class="nav">
    <div><b>🛒 Mineshop</b></div>
    <div>
        <a href="/">Dashboard</a>
        <a href="/escaner">Escáner</a>
    </div>
</div>

<div class="container">
CONTENT
</div>

</body>
</html>
"""

# ==========================
# DASHBOARD (TIEMPO REAL)
# ==========================
@app.route("/")
def home():
    return render_template_string(BASE.replace("CONTENT", """
    <div class="card">
        <h2>📊 Inventario en tiempo real</h2>
        <table id="tabla"></table>
    </div>

<script>
function cargar(){
fetch('/api/inv')
.then(r=>r.json())
.then(data=>{
let t="<tr><th>Producto</th><th>Cantidad</th></tr>";
for(let c in data){
t+=`<tr><td>${data[c].nombre}</td><td>${data[c].cantidad}</td></tr>`;
}
tabla.innerHTML=t;
});
}

setInterval(cargar,1000);
cargar();
</script>
"""))

# ==========================
# ESCÁNER PRO
# ==========================
@app.route("/escaner")
def escaner():
    return render_template_string(BASE.replace("CONTENT", """
<h2>📡 Escáner Mineshop</h2>

<p>Activa la cámara y escanea productos</p>

<button onclick="iniciar()">Activar cámara</button>
<button onclick="detener()">Detener</button>

<p id="estado"></p>

<div id="reader" style="width:300px;"></div>

<audio id="beep">
<source src="https://www.soundjay.com/buttons/sounds/beep-07.mp3" type="audio/mpeg">
</audio>

<script>
let scanner = null;
let ultimo = "";
let tiempo = 0;

function iniciar(){
    if(scanner){
        estado.innerText = "La cámara ya está activa";
        return;
    }

    scanner = new Html5Qrcode("reader");
    estado.innerText = "Solicitando cámara...";

    Html5Qrcode.getCameras().then(cams=>{
        if(!cams.length){
            estado.innerText = "No hay cámara disponible";
            return;
        }

        let cam = cams.find(c=>c.label.toLowerCase().includes("back")) || cams[0];

        scanner.start(
            cam.id,
            {fps:10, qrbox:250},
            txt=>{
                let ahora = Date.now();

                // 🚫 evitar duplicados rápidos
                if(txt === ultimo && (ahora - tiempo) < 2000){
                    return;
                }

                ultimo = txt;
                tiempo = ahora;

                estado.innerHTML = "✅ Escaneado: " + txt;
                document.getElementById("beep").play();

                fetch('/api/scan',{
                    method:'POST',
                    headers:{'Content-Type':'application/json'},
                    body:JSON.stringify({c:txt})
                });
            }
        );

    }).catch(err=>{
        estado.innerText = "❌ Debes permitir la cámara";
    });
}

function detener(){
    if(scanner){
        scanner.stop().then(()=>{
            scanner=null;
            estado.innerText="Cámara detenida";
            reader.innerHTML="";
        });
    }
}
</script>
"""))

# ==========================
# API
# ==========================
@app.route("/api/scan", methods=["POST"])
def scan_api():
    code = request.json["c"]

    if code in inventario:
        inventario[code]["cantidad"] += 1
    else:
        inventario[code] = {
            "nombre": mock.get(code, {"nombre":"Producto"})["nombre"],
            "cantidad": 1
        }

    return jsonify(ok=True)

@app.route("/api/inv")
def inv():
    return jsonify(inventario)

# ==========================
# RUN
# ==========================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True, ssl_context="adhoc")