import mysql.connector


def select(consulta):
    # Conectarse a la base de datos
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="academia"
    )

    # Crear un cursor
    cursor = conexion.cursor()

    # Ejecutar una consulta
    cursor.execute(consulta)

    # Obtener los resultados de la consulta
    resultados = cursor.fetchall()

    # Cerrar el cursor y la conexión
    cursor.close()
    conexion.close()

    return resultados
