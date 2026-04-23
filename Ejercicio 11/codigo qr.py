from flask import Flask, render_template_string, request, redirect, session, jsonify

app = Flask(_name_)
app.secret_key = "seguridad_basica_2026"

# Configuración de acceso simple
CREDENCIALES = {"usuario": "admin", "clave": "admin2026"}

HTML_BASE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Scanner Web Simple</title>
    <script src="https://unpkg.com/html5-qrcode"></script>
    <style>
        body { font-family: sans-serif; padding: 20px; max-width: 500px; margin: auto; background: #fafafa; }
        .box { border: 1px solid #ccc; padding: 20px; background: white; border-radius: 5px; }
        input { display: block; width: 100%; margin-bottom: 10px; padding: 8px; box-sizing: border-box; }
        button { width: 100%; padding: 10px; cursor: pointer; background: #333; color: white; border: none; }
        #reader { width: 100%; margin-top: 15px; }
        .log { margin-top: 20px; border-top: 1px solid #eee; padding-top: 10px; font-size: 0.9em; }
        .item { background: #f0f0f0; padding: 5px; margin-bottom: 5px; border-radius: 3px; }
    </style>
</head>
<body>
    <div class="box">
        {% if not session.get('auth') %}
            <h2>Ingreso</h2>
            <form method="POST">
                <input type="text" name="u" placeholder="Usuario" required>
                <input type="password" name="p" placeholder="Password" required>
                <button type="submit">Entrar</button>
            </form>
            {% if e %}<p style="color:red">{{ e }}</p>{% endif %}
        {% else %}
            <h2>Escanear</h2>
            <div id="reader"></div>
            <div class="log" id="historial">
                <strong>Resultados:</strong>
                <div id="lista"></div>
            </div>
            <p><a href="/salir">Cerrar sesión</a></p>
            <script>
                function onScanSuccess(decodedText) {
                    let lista = document.getElementById('lista');
                    let div = document.createElement('div');
                    div.className = 'item';
                    
                    // Lógica para detectar formato WIFI
                    if (decodedText.startsWith("WIFI:")) {
                        let red = decodedText.match(/S:(.*?);/);
                        let pass = decodedText.match(/P:(.*?);/);
                        div.innerHTML = <b>WIFI:</b> ${red ? red[1] : '?'}<br><b>PASS:</b> ${pass ? pass[1] : '?'};
                    } else {
                        div.innerText = "Texto: " + decodedText;
                    }
                    
                    lista.prepend(div);
                    fetch('/registro', {
                        method: 'POST',
                        headers: {'Content-Type': 'application/json'},
                        body: JSON.stringify({dato: decodedText})
                    });
                }

                let html5QrcodeScanner = new Html5QrcodeScanner("reader", { fps: 10, qrbox: 200 });
                html5QrcodeScanner.render(onScanSuccess);
            </script>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
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
    content = request.json
    print(f"Recibido: {content.get('dato')}")
    return jsonify({"msg": "ok"})

@app.route("/salir")
def salir():
    session.clear()
    return redirect("/")

if _name_ == "_main_":
    # Importante: Mantener ssl_context para uso de cámara
    app.run(host="0.0.0.0", port=5000, ssl_context='adhoc')