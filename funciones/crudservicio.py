import sqlite3
con=sqlite3.connect("db/Perseo.db")
micursor=con.cursor()

"""def insertar():
    tabla= 'tb_servicio'
    id_ser=int(input('ingrese el id del servicio: '))
    cant=int(input('ingrese la cantidad: '))
    id_tiposer=int(input('ingrese el id del tipo de servicio: '))
    id_fact=int(input('ingrese el id de la factura: '))
    sentencia=f"INSERT INTO {tabla} VALUES ('{id_ser}','{cant}','{id_tiposer}','{id_fact}')"
    micursor.execute(sentencia)
    con.commit()
    print('Registro Creado!!!!')
insertar()"""

"""def eliminar():
    tabla ='tb_servicio'
    campo = 'serv_idServicio'
    dato = int(input('ingrese el id del servicio: '))
    sentencia=f"DELETE FROM {tabla} WHERE {campo}='{dato}'"
    micursor.execute(sentencia)
    con.commit()
    print('Eliminación Exitosa!!!!')
eliminar()"""

"""def modificar():
    tabla ='tb_servicio'
    campo = input("ingrese el campo a modificar: ")
    dato = int(input("ingrese el dato: "))
    id = int(input("ingrese el id del servicio que desea modificar: "))
    sentencia=f"UPDATE {tabla} SET {campo}='{dato}'WHERE serv_idServicio={id}"
    micursor.execute(sentencia)
    con.commit()
    print('Modificación Exitosa!!!!')
modificar()"""

"""def consultar():
    tabla = 'tb_servicio'
    campo = input("ingrese el campo a consultar: ")
    operador = input("ingrese el operador para realizar la consulta: ")
    dato = int(input("ingrese el dato: "))
    sentencia=f"SELECT * FROM {tabla} WHERE {campo}{operador}'{dato}'"
    lista=micursor.execute(sentencia)
    return lista.fetchall()
print(consultar())"""

"""def consultartodo():
    tabla = 'tb_servicio'
    sentencia=f"SELECT * FROM {tabla}"
    lista=micursor.execute(sentencia)
    return lista.fetchall()
print(consultartodo())"""


