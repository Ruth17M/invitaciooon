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

 # Eliminar todos los invitados
def eliminar_todos_invitados():
        conn = sqlite3.connect("database.sqlite")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM invitados;")
        conn.commit()
        conn.close()
        print("🗑️ Todos los invitados han sido eliminados.")


if __name__ == "__main__":
   # crear_base_datos()


    # 1. Agregar una sola persona
    #  agregar_invitado("Nuevo Invitado", 2, "Juan, Ana")

    # 2. Agregar muchos a la vez
    nuevos_invitados = [
        ("Ruth Manríquez", 2, "Ruth Manríquez, Ethan Lemus"),
        ("Juan Lemus", 4, " Juan Lemus, Adriana Montelongo, Oziel Lemus, Maggie Chavez"),
        ("Jaime Fuerte", 4, "Jaime Fuerte, Rosario Gómez, Jonas Fuerte, Job Fuerte"),
        ("Jesse Cruz", 3, "Jesse Cruz, Elvia Salas, Amelia Fuerte"),
        ("Rosario Fuerte", 4, "Rosario Fuerte, Yaretzi Cruz, Citlalli Cruz, Saul Cruz"),
        ("Herminia Tavera", 7, "Herminia Tavera, Juan Fuerte, Magda Fuerte, Caro Fuerte, Diego Fuerte, Jesus Rios, Denisse"),
        ("Cesar Aranda", 2, "Cesar Aranda, Denisse Ontiveros"),
        ("Melissa Aranda", 3, "Melissa Aranda, Humberto Becerra, Matias Becerra"),
        ("Gammaliel Fuerte", 8, "Gammaliel Fuerte, Coco Muñoz, Jafet Fuerte, Josue Fuerte, Judith Fuerte, Hassiel Fuerte, Daniela Villagomez, Sandra Colorado"),
        ("Juanita Tavera", 4, "Juanita Tavera, Fer Aranda, Rene Cardona, Manuel Aranda"),
        ("Violeta Tavera", 5, "Violeta Tavera, Jesus Campos, Jonathan Campos, Veronica Campos, Angel Campos"),
        ("Jose Luis Chavez", 2, "Jose Luis Chavez, Lupita"),
        ("Pedro Salgado", 2, "Pedro Salgado, Rocio"),
        ("Martha Rocha", 1, "Martha Rocha"),
        ("Jaziel Miranda", 2, "Jaziel Miranda, Greys Padilla"),
        ("Laura Rocha", 2, "Laura Rocha, Martin Irena"),
        ("Familia Manriquez Fuerte", 8, "Mariano Manriquez, Miriam Fuerte, Baruc Manriquez, Mateo Manriquez, Fatima Manriquez, Esaú Manriquez, Guadalupe Reyes, Lucita Manriquez"),
        ("Ulises Escalante", 2, "Ulises Escalante, esposa"),
        ("Alex Balderas", 1, "Alex Balderas"),
        ("Marlenne Covarrubias", 1, "Marlenne Covarrubias"),
        ("César Limon", 1, "César Limon"),
        ("Berenice Porras", 3, "Berenice Porras, Juan Diaz, Nelly Diaz"),
        ("Juan de Dios Campos", 3, "Juan de Dios Campos, Gabriela, +1 niño"), 
        ("José de Jesús Campos", 4, "José de Jesús Campos, Magy, +2 niños"),
        ("Emmanuel Campos", 4, "Emmanuel Campos, +2 adultos y 1 niño"), 
        ("Juan Ramírez", 1, "Juan Ramírez"),
        ("David Alba", 1, "David Alba"),
        ("Martha Diaz", 2, "Martha Diaz, Ricardo Espinoza"),
        ("Alexa Azpeitia", 1, "Alexa Azpeitia"),
        ("Ana Reyes Zermeño", 1, "Ana Reyes Zermeño"),        
        ("Andrea Godinez", 1, "Andrea Godinez"),
        ("Maura de la Torre", 1, "Maura de la Torre"),
        ("Leonardo Martinez", 1, "Leonardo Martinez"),
        ("Milton Santoyo", 1, "Milton Santoyo"),
        ("Nubia Velazquez", 1, "Nubia Velazquez"),
        ("Regina Martinez", 1, "Regina Martinez"),
        ("Erick Torres", 1, "Erick Torres"), 
        ("Sandra Yunuen", 1, "Sandra Yunuen"),
        ("Saúl Lara", 1, "Saúl Lara"),
        ("Yaretzi Paola", 1, "Yaretzi Paola"),
        ("Regina Lozano", 1, "Regina Lozano"),
        ("Hasiel Lozano", 1, "Hasiel Lozano"),
        ("Mariana Jauregui", 1, "Mariana Jauregui"),
        ("Lizbeth Lopez", 1, "Lizbeth Lopez"),
        ("Regina", 1, "Regina"),
        ("Santiago Flores", 1, "Santiago Flores"),
        ("Evan", 1, "Evan"), 
        ("Santiago Flores", 1, "Santiago Flores"),
        ("Mauro Moreno", 1, "Mauro Moreno"),
        ("Ana", 1, "Ana"), 
        ("Jorge Herrera", 1, "Jorge Herrera"),
        ("Yojan Ramos", 1, "Yojan Ramos"),
        ("Omar Guerra", 1, "Omar Guerra"),
        ("Diana Zamarripa", 1, "Diana Zamarripa"),
        ("Dulce Medina", 3, "Dulce Medina, Issac Medina, Emmanuel Medina"), 
        ("Oscar Balandran", 2, "Oscar Balandran, Tere Rodriguez"), 
        ("Lucia Covarrubias", 1, "Lucia Covarrubias"), 
        ("Rodrigo Aranda", 5, "Rodrigo Aranda, Fernanda Aranda, Mariana Aranda, Rosy Guevara, Rodrigo Aranda"),
        ("Aranza Cruz", 1, "Aranza Cruz"),
        ("Santiago Fuentes", 1, "Santiago Fuentes"),
        ("Daniela Hernandez", 1, "Daniela Hernandez"), 
        ("Alondra", 1, "Alondra"), 
        ("Alejandro Mendoza", 1, "Alejandro Mendoza"),
        ("Fernando Ayala", 1, "Fernando Ayala"),
        ("Mireya Vazquez", 2, "Mireya Vazquez, Andrea Vazquez"),
        ("Alma Delia Tovar", 2, "Alma Delia Tovar, Alma Tovar"),
        ("Juan Reyes", 2, "Juan Reyes, Adelita"),
        ("Pablo Reyes", 2, "Pablo Reyes, Lupita"),
        ("Omar Reyes", 2, "Omar Reyes, esposa"),
        ("Mary Reyes", 2, "Mary Reyes, Manuel"),
        ("Coco Reyes", 2, "Coco Reyes, +1 adulto"),
        ("Fany Reyes", 3, "Fany Reyes, Ani Reyes, Maximiliano Reyes"),
        ("Cata Reyes", 2, "Cata Reyes, Yolanda Reyes"),
        ("Angelica Fuerte", 5, "Angelica Fuerte,Diana Fuerte, Jessenia Fuerte, José, +1 niño"),
        ("Carlos", 2, "Carlos Morales, Brenda Morales"),
        ("Lola Reyes", 4, "Lola Reyes, +3 adultos"),
        ("Ernesto Velazquez", 5, "Ernesto Velazquez, Lucy Muñoz, Jose Pablo Velazquez, Angela Velazquez, Marcela Velazquez"),
        ("Leticia Patiño", 1, "Leticia Patiño"), 
        ("Ulises Vargas", 3, "Ulises Vargas, Laura, 1 niño"),
        ("Trinidad  Martinez", 1, "Trinidad  Martinez"), 
        ("Elizabeth", 2, "Elizabeth, +1 adulto"),
        ("Fabian", 1, "Fabian"), 
        ("Esther",2, "Esther, +1 adulto"), 
        ("Claudia", 1, "Claudia"), 
        ("Martha", 1, "Martha"), 
        ("Mario Jasso", 1, "Mario Jasso"),
        ("Ximena Martinez",1, "Ximena Martinez"),
        ("Omar Morales", 1, "Omar Morales"),
        ("Maria Castillo", 1, "Maria Castillo"),
        ("Josafat Aguirre", 1, "Josafat Aguirre"),
        ("Andres Aguilera", 1, "Andres Aguilera"),
        ("Camila Liedo", 1, "Camila Liedo"),
        ("Mariana Ortiz", 1, "Mariana Ortiz")


    ]
    

    
    #agregar_varios_invitados(nuevos_invitados)


   # agregar_invitado("Blanca Rocha",3,"Blanca Rocha, Antonio Casanova, Refugio Manriquez")
   # agregar_invitado("Guadalupe Gonzalez",2,"Guadalupe Gonzalez, +1 adulto")
   # agregar_invitado("Pilar",2,"Pilar, +1 adulto")
   # agregar_invitado("Claudia Cayetano",2,"Claudia Cayetano, +1 adulto")
   # agregar_invitado("Alma Vareala",2,"Alma Varela, Lupita Valencia")
   # agregar_invitado("Anita",1,"Anita")
   # agregar_invitado("Maria de Jesus Fuerte",2,"Maria de Jesus Fuerte, +1 adulto")

    # editar_invitado(2, nuevo_nombre="Cristina Ramírez", nuevos_pases=4)
   

    # Llama a la función para eliminar todos los invitados
    #eliminar_todos_invitados()
    

  #  eliminar_invitado(154)
   # eliminar_invitado(180)
   # eliminar_invitado(199)

    agregar_invitado("Zoe Robledo",1,"Zoe Robledo")
    agregar_invitado("Ramses de la Torre",1,"Ramses de la Torre")
    agregar_invitado("Frida Franco",1,"Frida Franco")
    agregar_invitado("Arleth Diaz",1,"Arleth Diaz")
    agregar_invitado("Odette Angeles",1,"Odette Angeles")
    agregar_invitado("Uriel Patiño",1,"Uriel Patiño")
    agregar_invitado("Kamila Abdalah",1,"Kamila Abdalah")
    agregar_invitado("Antonio Santos",1,"Antonio Santos")
    ver_invitados()