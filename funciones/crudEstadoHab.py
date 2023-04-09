import sqlite3
con=sqlite3.connect('db/Perseo.db')
micursor=con.cursor()

def consuhab(tabla, campo, operador,dato):
    sentencia=f"SELECT * FROM {tabla} WHERE {campo}{operador}'{dato}'"
    #print(sentencia)
    lista=micursor.execute(sentencia)
    return lista.fetchall()
print(consuhab('tb_estadoHabitacion','esha_idEstadoHab','=','3'))

# en esta parte se puede consultar el estado la habitacion por el id 
#----------------------------------------------------------------------------------------------------------------

import sqlite3
con=sqlite3.connect('db/Perseo.db')
micursor=con.cursor()

def eliminar(tabla,campo,dato):
    sentencia=f"DELETE FROM {tabla} WHERE {campo}='{dato}'"
    micursor.execute(sentencia)
    con.commit()
    print('Eliminación Exitosa!!!!')

eliminar('tb_estadoHabitacion','esha_idestadoHab','3')

#en esta parte se puede eliminar una habitacion o en su defecto el estado de ella 
#-----------------------------------------------------------------------------------------------------------------------------
import sqlite3
con=sqlite3.connect('db/Perseo.db')
micursor=con.cursor()

def insertarhab(tabla,idhabi,estado):
    sentencia=f"INSERT INTO {tabla} VALUES ('{idhabi}','{estado}')"
    print(sentencia)
    micursor.execute(sentencia)
    con.commit()
    print('Registro Creado!!!!')

insertarhab('tb_estadoHabitacion','4','ocupada')

# en esta parte se puede agregar una habitacion y su estado 
#---------------------------------------------------------------------------------------------------------------------------

import sqlite3
con=sqlite3.connect('db/Perseo.db')
micursor=con.cursor()

def modificarhab(tabla,campo,dato,id):
    sentencia=f"UPDATE {tabla} SET {campo}='{dato}'WHERE id={id}"
    print(sentencia)
    micursor.execute(sentencia)
    con.commit()
    print('Modificación Exitosa!!!!')

modificarhab('tb_estadoHabitacion','esha_idEstadoHab','ocupada',1)

# en esta parte se puede modificar el estado de la habitacion, puede pasar de estar ocupada a disponible 

#consuhab()
#eliminar()
#insertarhab()
# modificarhab()
