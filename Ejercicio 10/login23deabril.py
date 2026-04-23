from flask import Flask, render_template_string, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = "super_clave_segura_2026"

# Credenciales correctas
USUARIO_VALIDO = "Admin"
PASSWORD_VALIDO = "Admin2026"

# HTML con estilo moderno (CSS integrado)
login_html = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Login Seguro</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #667eea, #764ba2);
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .login-box {
            background: white;
            padding: 40px;
            border-radius: 15px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.2);
            width: 300px;
            text-align: center;
        }
        input {
            width: 90%;
            padding: 10px;
            margin: 10px 0;
            border-radius: 8px;
            border: 1px solid #ccc;
        }
        button {
            background: #667eea;
            color: white;
            border: none;
            padding: 10px;
            width: 95%;
            border-radius: 8px;
            cursor: pointer;
        }
        button:hover {
            background: #5a67d8;
        }
        .error {
            color: red;
        }
    </style>
</head>
<body>
    <div class="login-box">
        <h2>🔐 Iniciar sesión</h2>
        <form method="POST">
            <input type="text" name="usuario" placeholder="Usuario" required>
            <input type="password" name="password" placeholder="Contraseña" required>
            <button type="submit">Entrar</button>
        </form>
        {% with messages = get_flashed_messages() %}
            {% if messages %}
                <p class="error">{{ messages[0] }}</p>
            {% endif %}
        {% endwith %}
    </div>
</body>
</html>
"""

home_html = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Inicio</title>
    <style>
        body {
            font-family: Arial;
            background: #1a202c;
            color: white;
            text-align: center;
            padding-top: 100px;
        }
        a {
            color: #63b3ed;
            text-decoration: none;
        }
    </style>
</head>
<body>
    <h1>🎉 Bienvenido {{ usuario }}</h1>
    <p>Acceso concedido correctamente</p>
    <a href="/logout">Cerrar sesión</a>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form["usuario"]
        password = request.form["password"]

        if usuario == USUARIO_VALIDO and password == PASSWORD_VALIDO:
            session["usuario"] = usuario
            return redirect(url_for("home"))
        else:
            flash("❌ Credenciales incorrectas")

    return render_template_string(login_html)

@app.route("/home")
def home():
    if "usuario" in session:
        return render_template_string(home_html, usuario=session["usuario"])
    return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)