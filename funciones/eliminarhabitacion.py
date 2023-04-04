import sqlite3
con=sqlite3.connect('db/Perseo.db')
micursor=con.cursor()

def eliminar(tabla,campo,dato):
    sentencia=f"DELETE FROM {tabla} WHERE {campo}='{dato}'"
    micursor.execute(sentencia)
    con.commit()
    print('Eliminación Exitosa!!!!')

eliminar('tb_estadoHabitacion','esha_idestadoHab','3')