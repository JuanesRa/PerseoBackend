import sqlite3
con=sqlite3.connect('db/Perseo.db')
micursor=con.cursor()

def insertar(tabla,idhabi,estado):
    sentencia=f"INSERT INTO {tabla} VALUES ('{idhabi}','{estado}')"
    print(sentencia)
    micursor.execute(sentencia)
    con.commit()
    print('Registro Creado!!!!')

insertar('tb_estadoHabitacion','4','ocupada')