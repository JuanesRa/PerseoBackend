import sqlite3
con=sqlite3.connect("db/Perseo.db")
micursor=con.cursor()

def insertartipo():
    tabla= 'tb_tipoServicio'
    tise_idTipoServicio=int(input('ingrese el id del tipo de servicio: '))
    tise_tipo=input('ingrese el tipo de servicio: ')
    tise_precio=int(input('ingrese el precio del servicio: '))
    sentencia=f"INSERT INTO {tabla} VALUES ('{tise_idTipoServicio}','{tise_tipo}','{tise_precio}')"
    micursor.execute(sentencia)
    con.commit()
    print('Registro Creado!!!!')


def eliminartipo():
    tabla ='tb_tipoServicio'
    campo = 'tise_idTipoServicio'
    dato = int(input('ingrese el id del tipo de servicio: '))
    sentencia=f"DELETE FROM {tabla} WHERE {campo}='{dato}'"
    micursor.execute(sentencia)
    con.commit()
    print('Eliminación Exitosa!!!!')


def modificartipo():
    tabla ='tb_tipoServicio'
    campo = input("ingrese el campo a modificar: ")
    dato = int(input("ingrese el dato: "))
    id = int(input("ingrese el id del servicio que desea modificar: "))
    sentencia=f"UPDATE {tabla} SET {campo}='{dato}'WHERE tise_idTipoServicio={id}"
    micursor.execute(sentencia)
    con.commit()
    print('Modificación Exitosa!!!!')


def consultartipo():
    tabla = 'tb_tipoServicio'
    campo = input("ingrese el campo a consultar: ")
    operador = input("ingrese el operador para realizar la consulta: ")
    dato = int(input("ingrese el dato: "))
    sentencia=f"SELECT * FROM {tabla} WHERE {campo}{operador}'{dato}'"
    lista=micursor.execute(sentencia)
    return lista.fetchall()
    print(consultartipo())

def reporteTipoServicio():
    while True:
        print('Reporte Tipo Servicios:\n 1-Crear reporte\n 2-Ver reporte\n 3-Eliminar reporte')
        ctrl=str(input('Seleccione opción: '))
        match ctrl:
            case '0':
                break
            case '1':
                try:
                    import os
                    import datetime as d
                    from sys import path
                    path.append('../PerseoBackend/clases')
                    from TipoServicio import  tiposer
                    sentencia=f"SELECT * FROM tb_tipoServicio"
                    lista=micursor.execute(sentencia)
                    ite=lista.fetchall()
                    #----------------------------------------------------
                    instance_tipo=[]
                    ts=[]
                    dia_presente= d.date.today()
                    nombre_repor=str(input('Nombre del reporte a crear: '))
                    nombre_com=f'{nombre_repor}{dia_presente}'
                    if os.path.exists(f'reportes/{nombre_com}'):
                        raise FileExistsError
                    else:
                        for i in ite:
                            ts.append(i)
                        
                        for campo in ts:
                            objtipo = tiposer(campo[0],campo[1],campo[2])
                            instance_tipo.append(objtipo)

                        with open(f'reportes/{nombre_com}','a') as flujo: 
                            for i in instance_tipo:
                                flujo.write (str(i.get_idTipo())+','+str(i.get_tipo())+','+str(i.get_precio())+'\n')
                        print('Creación de reporte exitosa!!')
                        print('')
                except FileExistsError:
                    print('Error!! el reporte',nombre_com,'YA existe')
                    print('')
            case '2':
                try:
                    import os
                    nombre_repor = str(input('Nombre del reporte que quiere ver: '))
                    ruta_archivo = f'../PerseoBackend/reportes/{nombre_repor}'

                    if os.path.exists(ruta_archivo):
                        with open(f'reportes/{nombre_repor}', 'r') as flujo:
                            lineas = flujo.readlines()
                            for linea in lineas:
                                campos = linea.strip().split(',')
                                print(int(campos[0]),' ', end='')
                                print(campos[1],' ', end='')
                                print(campos[2])

                            print('')
                    else:
                        raise FileNotFoundError
                        
                except FileNotFoundError:
                    print(f'El archivo {nombre_repor} no existe')
                    print('')
                
            case '3':
                try:
                    import os

                    nombre_repor = input('Nombre del reporte a eliminar: ')
                    ruta_archivo = f'../PerseoBackend/reportes/{nombre_repor}'

                    if os.path.exists(ruta_archivo):
                        os.remove(ruta_archivo)
                        print('Eliminación de reporte exitosa!!')
                        print('')
                    else:
                        raise FileNotFoundError
                        
                except FileNotFoundError:
                    print(f'El archivo {ruta_archivo} no existe')
                    print('')

                
            case _:
                print('Esta opción no existe\n')  

reporteTipoServicio()


#insertartipo()
#eliminartipo()
#modificartipo()
#consultartipo()

