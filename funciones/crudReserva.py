import sqlite3
con=sqlite3.connect('db/Perseo.db')
micursor=con.cursor()

def seleccion(tabla, campo, operador,dato):
    latabla= 'tb_reserva'
    elcampo= 'rese_idReserva'
    eloperador= '='
    sentencia=f"SELECT * FROM {tabla} WHERE {campo}{operador}'{dato}'"
    #print(sentencia)
    lista=micursor.execute(sentencia)
    print('id reserva--', 'cantidad habitacion--','numero de personas-- ','fecha ingreso--', 'fecha salida-- ','id usuario--','--numero habitacion')
    seleccion(latabla,elcampo,eloperador,'1')
    return lista.fetchall()
#print(seleccion())
# en esta parte se pude consultar las reservas que ya esten realizadas 
#--------------------------------------------------------------------------------------------------------------------------------------------------------------

import sqlite3
con=sqlite3.connect('db/Perseo.db')
micursor=con.cursor()

def eliminarre(tabla,campo,dato):
    tbre= 'tb_reserva'
    cam= 'rese_idReserva'
    sentencia=f"DELETE FROM {tabla} WHERE {campo}='{dato}'"
    micursor.execute(sentencia)
    con.commit()
    print('Eliminación Exitosa!!!!')
    eliminarre(tbre,cam,5)
#print(eliminarre())

# en esta parte se elimina una reserva con el id de la reserva 
#---------------------------------------------------------------------------------------------------------------------------------------------------------------

import sqlite3
con=sqlite3.connect('db/Perseo.db')
micursor=con.cursor()

def insertarre(tabla,idre,canhab,numpersonas,fechaini,fechafin,idusuario,idhabi):
    sentencia=f"INSERT INTO {tabla} VALUES ('{idre}','{canhab}','{numpersonas}','{fechaini}','{fechafin}','{idusuario}','{idhabi}')"
    print(sentencia)
    micursor.execute(sentencia)
    con.commit()
    print('Registro Creado!!!!')

#insertarre('tb_reserva',5,5,5,'29-03-2023','30-03-2023',19999,909)

# en esta parte se inserta la reserva con los datos pedidos 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import sqlite3
con=sqlite3.connect('db/Perseo.db')
micursor=con.cursor()

def modificarre(tabla,campo,dato,id):
    sentencia=f"UPDATE {tabla} SET {campo}='{dato}'WHERE id={id}"
    print(sentencia)
    micursor.execute(sentencia)
    con.commit()
    print('Modificación Exitosa!!!!')

#modificarre('tb_reserva','rese_numPersonas',8,1)

#en esta parte se pueden hacer modificaciones de la reserva como el numero de perosnas etc...




#seleccion()
#eliminarre()
#insertarre()
#modificarre()