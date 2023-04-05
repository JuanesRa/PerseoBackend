import sqlite3
con=sqlite3.connect('db/Perseo.db')
micursor=con.cursor()

def seleccion(tabla, campo, operador,dato):
    sentencia=f"SELECT * FROM {tabla} WHERE {campo}{operador}'{dato}'"
    #print(sentencia)
    lista=micursor.execute(sentencia)
    return lista.fetchall()
print('id reserva--', 'cantidad habitacion--','numero de personas-- ','fecha ingreso--', 'fecha salida-- ','id usuario--','--numero habitacion')
print(seleccion('tb_reserva','rese_idReserva','=','1'))