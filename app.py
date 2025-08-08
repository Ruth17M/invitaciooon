from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__, static_folder="static", template_folder="templates")
DB = "database.sqlite"



@app.route("/")
def index():
    return render_template("index.html")  # Esto carga tu HTML principal


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


@app.route("/buscar")
def buscar():
    nombre = request.args.get("nombre", "").strip()
    conn = sqlite3.connect("database.sqlite")
    cursor = conn.cursor()

    # Buscar el nombre entre los invitados registrados
    cursor.execute("SELECT nombre, pases, invitados FROM invitados")
    registros = cursor.fetchall()
    conn.close()

    for registro in registros:
        nombre_titular, pases, invitados_str = registro
        lista_invitados = [n.strip() for n in invitados_str.split(",")]

        if nombre in lista_invitados:
            return jsonify({
                "encontrado": True,
                "pases": pases,
                "invitados": lista_invitados
            })

    return jsonify({"encontrado": False})



if __name__ == "__main__":
    app.run(debug=True)