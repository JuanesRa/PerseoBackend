import sqlite3
con=sqlite3.connect('db/Perseo.db')
micursor=con.cursor()

def modificar(tabla,campo,dato,id):
    sentencia=f"UPDATE {tabla} SET {campo}='{dato}'WHERE id={id}"
    print(sentencia)
    micursor.execute(sentencia)
    con.commit()
    print('Modificación Exitosa!!!!')

modificar('tb_reserva','rese_numPersonas',8,1)