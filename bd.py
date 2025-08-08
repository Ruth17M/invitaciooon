import sqlite3

def crear_base_datos():
    conn = sqlite3.connect("database.sqlite")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS invitados (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        pases INTEGER NOT NULL,
        invitados TEXT
    );
    """)

    conn.commit()
    conn.close()
    print("Base de datos y tabla creadas.")


# Agregar invitado
def agregar_invitado(nombre, pases, invitados):
    conn = sqlite3.connect("database.sqlite")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO invitados (nombre, pases, invitados) VALUES (?, ?, ?);
    """, (nombre, pases, invitados))

    conn.commit()
    conn.close()
    print(f"✅ Invitado '{nombre}' agregado con {pases} pase(s).")


#Agregar varios invitados
def agregar_varios_invitados(lista_invitados):
    conn = sqlite3.connect("database.sqlite")
    cursor = conn.cursor()

    cursor.executemany("""
    INSERT INTO invitados (nombre, pases, invitados) VALUES (?, ?, ?);
    """, lista_invitados)

    conn.commit()
    conn.close()
    print("✅ Lista de invitados agregada.")




# Ver todos los invitados
def ver_invitados():
    conn = sqlite3.connect("database.sqlite")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM invitados;")
    resultados = cursor.fetchall()

    conn.close()

    print("\n📋 Lista de invitados:")
    for invitado in resultados:
        print(f"ID: {invitado[0]}, Nombre: {invitado[1]}, Pases: {invitado[2]}, Invitados: {invitado[3]}")


# Editar un invitado por ID
def editar_invitado(id, nuevo_nombre=None, nuevos_pases=None, nuevos_invitados=None):
    conn = sqlite3.connect("database.sqlite")
    cursor = conn.cursor()

    # Obtener datos actuales
    cursor.execute("SELECT nombre, pases, invitados FROM invitados WHERE id = ?;", (id,))
    resultado = cursor.fetchone()

    if resultado:
        nombre_actual, pases_actual, invitados_actuales = resultado
        nuevo_nombre = nuevo_nombre or nombre_actual
        nuevos_pases = nuevos_pases if nuevos_pases is not None else pases_actual
        nuevos_invitados = nuevos_invitados or invitados_actuales

        cursor.execute("""
        UPDATE invitados SET nombre = ?, pases = ?, invitados = ? WHERE id = ?;
        """, (nuevo_nombre, nuevos_pases, nuevos_invitados, id))

        conn.commit()
        print(f"✏️ Invitado con ID {id} actualizado.")
    else:
        print(f"No se encontró ningún invitado con ID {id}.")

    conn.close()


# Eliminar invitado por ID
def eliminar_invitado(id):
    conn = sqlite3.connect("database.sqlite")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM invitados WHERE id = ?;", (id,))
    conn.commit()
    conn.close()
    print(f"🗑️ Invitado con ID {id} eliminado.")


if __name__ == "__main__":
   # crear_base_datos()

    # Solo descomenta una de las siguientes opciones según lo que quieras hacer:

    # 1. Agregar una sola persona
    # agregar_invitado("Nuevo Invitado", 2, "Juan, Ana")

    # 2. Agregar muchos a la vez
  #  nuevos_invitados = [
   #      ("Carlos Gómez", 2, "María, Tomás"),
    #     ("Lucía Ramírez", 1, "Invitado especial"),
    #]
    #agregar_varios_invitados(nuevos_invitados)


    ver_invitados()

    # editar_invitado(2, nuevo_nombre="Cristina Ramírez", nuevos_pases=4)

    # eliminar_invitado(3)