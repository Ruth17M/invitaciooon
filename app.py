from flask import Flask, request, jsonify, render_template
import sqlite3, unicodedata

app = Flask(__name__, static_folder="static", template_folder="templates")
DB = "database.sqlite"



@app.route("/")
def index():
    return render_template("index.html")  # Esto carga tu HTML principal


def normalizar_texto(texto):
    texto = texto.strip().lower()
    texto = unicodedata.normalize('NFD', texto)
    texto = ''.join(c for c in texto if unicodedata.category(c) != 'Mn')  # elimina tildes
    return texto

@app.route("/buscar")
def buscar():
    nombre_raw = request.args.get("nombre", "").strip()
    nombre_normalizado = normalizar_texto(nombre_raw)

    conn = sqlite3.connect("database.sqlite")
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, pases, invitados FROM invitados")
    registros = cursor.fetchall()
    conn.close()

    for registro in registros:
        nombre_titular, pases, invitados_str = registro
        lista_invitados = [n.strip() for n in invitados_str.split(",")]

        # normaliza cada nombre en la lista
        lista_normalizada = [normalizar_texto(n) for n in lista_invitados]

        if nombre_normalizado in lista_normalizada:
            return jsonify({
                "encontrado": True,
                "pases": pases,
                "invitados": lista_invitados  # estos se devuelven con acentos y capitalización original
            })

    return jsonify({"encontrado": False})

# Obtener todos los invitados
@app.route("/invitados", methods=["GET"])
def get_invitados():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM invitados")
    invitados = cursor.fetchall()
    conn.close()

    resultado = []
    for inv in invitados:
        resultado.append({
            "id": inv[0],
            "nombre": inv[1],
            "pases": inv[2],
            "invitados": inv[3]
        })
    return jsonify(resultado)

# Agregar un invitado
@app.route("/invitados", methods=["POST"])
def add_invitado():
    data = request.json
    nombre = data["nombre"]
    pases = data["pases"]
    invitados = data["invitados"]

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO invitados (nombre, pases, invitados) VALUES (?, ?, ?);",
                   (nombre, pases, invitados))
    conn.commit()
    conn.close()
    return jsonify({"mensaje": "Invitado agregado"}), 201




if __name__ == "__main__":
    app.run(debug=True)