import sqlite3

con = sqlite3.connect('db/Perseo.db')
micursor = con.cursor()

def consuhab(tabla, campo, operador, dato):
    sentencia = f"SELECT * FROM {tabla} WHERE {campo}{operador}'{dato}'"
    #print(sentencia)
    lista = micursor.execute(sentencia)
    return lista.fetchall()

def eliminar(tabla, campo, dato):
    sentencia = f"DELETE FROM {tabla} WHERE {campo}='{dato}'"
    micursor.execute(sentencia)
    con.commit()
    print('Eliminación Exitosa!!!!')

def insertarhab(tabla, idhabi, estado):
    sentencia = f"INSERT INTO {tabla} VALUES ('{idhabi}','{estado}')"
    micursor.execute(sentencia)
    con.commit()
    print('Registro Creado!!!!')

def modificarhab(tabla, campo, dato, id):
    sentencia = f"UPDATE {tabla} SET {campo}='{dato}' WHERE id={id}"
    micursor.execute(sentencia)
    con.commit()
    print('Modificación Exitosa!!!!')

while True:
    print("Bienvenido al menú")
    print("1. Consultar estado de la habitación por ID")
    print("2. Eliminar una habitación o su estado")
    print("3. Agregar una habitación y su estado")
    print("4. Modificar el estado de una habitación")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        tabla = 'tb_estadoHabitacion'
        campo = 'esha_idEstadoHab'
        operador = '='
        dato = input("Introduzca el ID de la habitación a consultar: ")
        resultado = consuhab(tabla, campo, operador, dato)
        print(resultado)
    elif opcion == "2":
        tabla = 'tb_estadoHabitacion'
        campo = 'esha_idestadoHab'
        dato = input("Introduzca el ID de la habitación o estado a eliminar: ")
        eliminar(tabla, campo, dato)
    elif opcion == "3":
        tabla = 'tb_estadoHabitacion'
        idhabi = input("Introduzca el ID de la habitación a agregar: ")
        estado = input("Introduzca el estado de la habitación a agregar: ")
        insertarhab(tabla, idhabi, estado)
    elif opcion == "4":
        tabla = 'tb_estadoHabitacion'
        campo = 'esha_idEstadoHab'
        dato = input("Introduzca el nuevo estado de la habitación: ")
        id = input("Introduzca el ID de la habitación a modificar: ")
        modificarhab(tabla, campo, dato, id)
    elif opcion == "5":
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción del menú.")


# en esta parte se puede modificar el estado de la habitacion, puede pasar de estar ocupada a disponible 

#consuhab()
#eliminar()
#insertarhab()
# modificarhab()
