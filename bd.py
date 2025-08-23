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


    # 1. Agregar una sola persona
    #  agregar_invitado("Nuevo Invitado", 2, "Juan, Ana")

    # 2. Agregar muchos a la vez
    nuevos_invitados = [
        ("Ruth Manríquez", 2, "Ruth Manríquez, Ethan Lemus"),
        ("Juan Lemus", 5, " Juan Lemus, Adriana Montelongo, Oziel Lemuz, Maggie Chavez"),
        ("Jaime Fuerte", 4, "Jaime Fuerte, Rosario Gómez, Jonas Fuerte, Job Fuerte"),
        ("Jesse Fuerte", 3, "Jesse Fuerte, Elvia Salas, Amy Fuerte"),
        ("Rosario Fuerte", 4, "Rosario Fuerte, Yaretzi Fuerte, Citlalli Fuerte, Saul Fuerte"),
        ("Herminia Tavera", 7, "Herminia Tavera, Juan Fuerte, Magda Fuerte, Caro Fuerte, Diego Fuerte, + 2"),
        ("Cesar Aranda", 2, "Cesar Aranda, Denisse Ontiveros"),
        ("Melissa Aranda", 2, "Melissa Aranda, Humberto Becerra, Matias Becerra"),
        ("Gammaliel Fuerte", 8, "Gammaliel Fuerte, Coco Muñoz, Jafet Fuerte, Josue Fuerte, Judith Fuerte, Hassiel Fuerte, + 2"),
        ("Juanita Tavera", 4, "Juanita Tavera, Fer Aranda, Rene Cardona"),
        ("Violeta Tavera", 5, "Violeta Tavera, + 4"),
        ("Rosario Fuerte", 4, "Rosario Fuerte, Yaretzi Fuerte, Citlalli Fuerte, Saul Fuerte"),
        ("Jose Luis Chavez", 5, "Jose Luis Chavez, +4"),
        ("Familia Irena Rocha", 5, "Laura Rocha, +1"),
        ("Familia Salgado", 2, "+2"),
        ("Martha Rocha", 1, "Martha Rocha"),
        ("Jaziel Miranda", 2, "Jaziel Miranda, Greys Padilla"),
        ("Laura Rocha", 2, "Laura Rocha, Martin Irena"),
        ("Familia Manriquez Fuerte", 9, "Mariano Manriquez, Miriam Fuerte, Ruth Manriquez, Baruc Manriquez, Mateo Manriquez, Fatima Manriquez, Esaú Manriquez, Guadalupe Reyes, Lucita Manriquez"),
        ("Ulises Escalante", 2, "Ulises Escalante, +1 adulto"),
        ("Ulises Vargas",3, "Ulises Vargas, +1 adulto y 1 niño"),
        ("Alex Balderas", 1, "Alex Balderas"),
        ("Marlene", 2, "Marlene, +1"),
        ("César", 1, "César"),
        ("Belen Porras", 3, "Belen Porras, Juan Diaz, Nelly Diaz"),
        ("Juan de Dios Campos", 2, "Juan de Dios Campos, Gabriela, +1 niño"),
        ("José de Jesús Campos", 2, "José de Jesús Campos, Magy, +2 niños"),
        ("Emmanuel Campos", 2, "Emmanuel Campos, +1 adulto y 1 niño"),
        ("Pbr. Juan Ramírez", 1, "Pbr. Juan Ramírez"),
        ("Sr. Cura David Alba", 1, "Sr. Cura David Alba"),
        ("Martha Diaz", 2, "Martha Diaz, Ricardo Espinoza"),
        ("Alexa Azpeitia", 1, "Alexa Azpeitia"),
        ("Ana Reyes", 1, "Ana Reyes"),        
        ("Andrea Godinez", 1, "Andrea Godinez"),
        ("Maura de la Torre", 1, "Maura de la Torre"),
        ("Leonardo Martinez", 1, "Leonardo Martinez"),
        ("Milton Santoyo", 1, "Milton Santoyo"),
        ("Nubia Velazquez", 1, "Nubia Velazquez"),
        ("Regina Martinez", 1, "Regina Martinez"),
        ("Erick", 1, "Erick"),
        ("Sandra Yunuen", 1, "Sandra Yunuen"),
        ("Saúl Lara", 1, "Saúl Lara"),
        ("Yaretzi Paola", 1, "Yaretzi Paola"),
        ("Regina Lozano", 1, "Regina Lozano"),
        ("Hasiel Lozano", 1, "Hasiel Lozano"),
        ("Mariana Jauregui", 1, "Mariana Jauregui"),
        ("Liz", 1, "Liz"),
        ("Regina", 1, "Regina"),
        ("Santiago Flores", 1, "Santiago Flores"),
        ("Evan", 1, "Evan"),
        ("Santiago Flores", 1, "Santiago Flores"),
        ("Evan", 1, "Evan"),
        ("Mauro Moreno", 1, "Mauro Moreno"),
        ("Ana", 1, "Ana"),
        ("Jorge Herrera", 1, "Jorge Herrera"),
        ("Yojan Ramos", 1, "Yojan Ramos"),
        ("Omar Guerra", 1, "Omar Guerra"),
        ("Flor Hidalgo", 1, "Flor Hidalgo"),
        ("Diana GJ", 1, "Diana GJ"),
        ("Dulce", 3, "Dulce, Issac, Emmanuel GJ"),
        ("Emilio GJ", 1, "Emilio GJ"),
        ("Karol GJ", 1, "Karol GJ"),
        ("Oscar GJ", 2, "Oscar GJ, Tere GJ"),
        ("Lucia GJ", 1, "Lucia GJ"),
        ("Sayan GJ", 1, "Sayan GJ"),
        ("Familia Aranda Guevara", 5, "Familia Aranda Guevara (5 adultos)"),
        ("Aranza", 1, "Aranza"),
        ("Santiago Fuentes", 1, "Santiago Fuentes"),
        ("Daniela", 1, "Daniela"),
        ("Alondra", 1, "Alondra"),
        ("Alejandro Mendoza", 1, "Alejandro Mendoza"),
        ("Fernando Ayala", 1, "Fernando Ayala"),
        ("Mireya Vazquez", 2, "Mireya Vazquez, Andrea Vazquez"),
        ("Alma Delia Tovar", 2, "Alma Delia Tovar, Alma Tovar"),
        ("Juan Reyes", 2, "Juan Reyes, Adelita"),
        ("Pablo Reyes", 2, "Pablo Reyes, Lupita"),
        ("Omar Reyes", 2, "Omar Reyes, +1"),
        ("Mary Reyes", 2, "Mary Reyes, Manuel"),
        ("Coco Reyes", 2, "Coco Reyes, +1"),
        ("Fany Reyes", 2, "Fany Reyes, Ani Reyes"),
        ("Don Chano", 1, "Don Chano"),
        ("Cata Reyes", 2, "Cata Reyes, Yolanda Reyes"),
        ("Angelica Fuerte", 4, "Angelica Fuerte,Diana Fuerte, Jessenia Fuerte, José, +1 niño"),
        ("Carlos", 2, "Carlos, Brenda"),
        ("Lola", 4, "Lola Reyes, +3 adultos"),
        ("Ernesto", 5, "Ernesto, Lucy, Pablo, Angela, Marcela"),
        ("Marlene Covarrubias", 1, "Marlene Covarrubias"),
        ("Leticia Patiño", 1, "Leticia Patiño"),
        ("Ulises Vargas", 3, "Ulises Vargas, Laura, 1 niño"),
        ("Trini", 1, "Trini"),
        ("Elizabeth", 2, "Elizabeth, 1 adulto"),
        ("Fabian", 1, "Fabian"),
        ("Esther",2, "Esther, +1 adulto"),
        ("Claudia", 1, "Claudia"),
        ("Maestra Paty", 1, "Maestra Paty"),
        ("Mario Jasso", 2, "Mario Jasso, +1"),
        ("Ximena Martinez",1, "Ximena Martinez")


    ]
    
    agregar_varios_invitados(nuevos_invitados)




    # editar_invitado(2, nuevo_nombre="Cristina Ramírez", nuevos_pases=4)

    #eliminar_invitado(9)
    

    ver_invitados()