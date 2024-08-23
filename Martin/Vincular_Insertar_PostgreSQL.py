import mysql.connector

# Funciones para insertar el estado en postgreSQL
def insertarOrganismo1(tiempo,largo,ancho,forma,tipo,estado):
    conn = mysql.connector.connect(
        host="localhost",
        database="infraestructura",
        user="root",
        password="1234"
    )
    cur = conn.cursor()

    query = "INSERT INTO organismo_1 (tiempo, largo, ancho, forma, tipo, estado) VALUES (%s, %s, %s, %s, %s, %s)"
    data = (tiempo,largo,ancho,forma,tipo,estado)

    cur.execute(query, data)
    conn.commit()

    cur.close()
    conn.close()

def insertarOrganismo2 (tiempo,largo,ancho,forma,tipo,estado):
    conn = mysql.connector.connect(
        host="localhost",
        database="infraestructura",
        user="root",
        password="1234"
    )
    cur = conn.cursor()

    query = "INSERT INTO organismo_2 (tiempo, largo, ancho, forma, tipo, estado) VALUES (%s, %s, %s, %s, %s, %s)"
    data = (tiempo,largo,ancho,forma,tipo,estado)

    cur.execute(query, data)
    conn.commit()

    cur.close()
    conn.close()

def insertarEstado2 (tiempo,largo,ancho,forma,tipo,estado):
    conn = mysql.connector.connect(
        host="localhost",
        database="infraestructura",
        user="root",
        password="1234"
    )
    cur = conn.cursor()

    query = "INSERT INTO organismo_2 (tiempo, largo, ancho, forma, tipo, estado) VALUES (%s, %s, %s, %s, %s, %s)"
    data = (tiempo,largo,ancho,forma,tipo,estado)

    cur.execute(query, data)
    conn.commit()

    cur.close()
    conn.close()

def insertarDesconocido(tiempo,largo,ancho,forma,estado):
    conn = mysql.connector.connect(
        host="localhost",
        database="infraestructura",
        user="root",
        password="1234"
    )
    cur = conn . cursor ()

    query = "INSERT INTO desconocido (tiempo, largo, ancho, forma, estado) VALUES (%s, %s, %s, %s, %s)"
    data = (tiempo,largo,ancho,forma,estado)

    cur.execute(query, data)
    conn.commit()

    cur.close()
    conn.close()


