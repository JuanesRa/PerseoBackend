import sqlite3
con=sqlite3.connect("db/Perseo.db")
micursor=con.cursor()

"""def insertartipo():
    tabla= 'tb_tipoServicio'
    tise_idTipoServicio=int(input('ingrese el id del tipo de servicio: '))
    tise_tipo=input('ingrese el tipo de servicio: ')
    tise_precio=int(input('ingrese el precio del servicio: '))
    sentencia=f"INSERT INTO {tabla} VALUES ('{tise_idTipoServicio}','{tise_tipo}','{tise_precio}')"
    micursor.execute(sentencia)
    con.commit()
    print('Registro Creado!!!!')
insertartipo()"""

"""def eliminartipo():
    tabla ='tb_tipoServicio'
    campo = 'tise_idTipoServicio'
    dato = int(input('ingrese el id del tipo de servicio: '))
    sentencia=f"DELETE FROM {tabla} WHERE {campo}='{dato}'"
    micursor.execute(sentencia)
    con.commit()
    print('Eliminación Exitosa!!!!')
eliminartipo()"""

"""def modificartipo():
    tabla ='tb_tipoServicio'
    campo = input("ingrese el campo a modificar: ")
    dato = int(input("ingrese el dato: "))
    id = int(input("ingrese el id del servicio que desea modificar: "))
    sentencia=f"UPDATE {tabla} SET {campo}='{dato}'WHERE tise_idTipoServicio={id}"
    micursor.execute(sentencia)
    con.commit()
    print('Modificación Exitosa!!!!')
modificartipo()"""

"""def consultartipo():
    tabla = 'tb_tipoServicio'
    campo = input("ingrese el campo a consultar: ")
    operador = input("ingrese el operador para realizar la consulta: ")
    dato = int(input("ingrese el dato: "))
    sentencia=f"SELECT * FROM {tabla} WHERE {campo}{operador}'{dato}'"
    lista=micursor.execute(sentencia)
    return lista.fetchall()
print(consultartipo())"""

"""def consultartodotipo():
    tabla = 'tb_tipoServicio'
    sentencia=f"SELECT * FROM {tabla}"
    lista=micursor.execute(sentencia)
    return lista.fetchall()
print(consultartodotipo())"""
