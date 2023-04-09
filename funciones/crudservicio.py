import sqlite3
con=sqlite3.connect("db/Perseo.db")
micursor=con.cursor()

def insertar():
    print('Ingrese los datos para un nuevo registro')
    tabla= 'tb_servicio'
    id_ser=int(input('ingrese el id del servicio: '))
    cant=int(input('ingrese la cantidad: '))
    id_tiposer=int(input('ingrese el id del tipo de servicio: '))
    id_fact=int(input('ingrese el id de la factura: '))
    sentencia=f"INSERT INTO {tabla} VALUES ('{id_ser}','{cant}','{id_tiposer}','{id_fact}')"
    micursor.execute(sentencia)
    con.commit()
    print('Registro Creado!!!!')


def eliminar():
    print('Ingrese el id del servicio para eliminar el registro')
    tabla ='tb_servicio'
    campo = 'serv_idServicio'
    dato = int(input('ingrese el id del servicio: '))
    sentencia=f"DELETE FROM {tabla} WHERE {campo}='{dato}'"
    micursor.execute(sentencia)
    con.commit()
    print('Eliminación Exitosa!!!!')


def modificar():
    print('Ingrese los datos para modificar un registro')
    tabla ='tb_servicio'
    campo = input("ingrese el campo a modificar: ")
    dato = int(input("ingrese el dato: "))
    id = int(input("ingrese el id del servicio que desea modificar: "))
    sentencia=f"UPDATE {tabla} SET {campo}='{dato}'WHERE serv_idServicio={id}"
    micursor.execute(sentencia)
    con.commit()
    print('Modificación Exitosa!!!!')


def consultartodo():
    print('Los regitros de las tablas: ')
    tabla = 'tb_servicio'
    sentencia=f"SELECT * FROM {tabla}"
    lista=micursor.execute(sentencia)
    return lista.fetchall()
    print(consultartodo())

def reporteServicios():
    while True:
        print('Reporte Servicios:\n 1-Crear reporte\n 2-Ver reporte\n 3-Eliminar reporte')
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
                    from Servicio import  servicio
                    sentencia=f"SELECT * FROM tb_servicio"
                    lista=micursor.execute(sentencia)
                    ite=lista.fetchall()
                    #----------------------------------------------------
                    instance_servicios=[]
                    servicios=[]
                    dia_presente= d.date.today()
                    nombre_repor=str(input('Nombre del reporte a crear: '))
                    nombre_com=f'{nombre_repor}{dia_presente}'
                    if os.path.exists(f'reportes/{nombre_com}'):
                        raise FileExistsError
                    else:
                        for i in ite:
                            servicios.append(i)
                        
                        for campo in servicios:
                            objServicio=servicio(campo[0],campo[1],campo[2],campo[3])
                            instance_servicios.append(objServicio)

                        with open(f'reportes/{nombre_com}','a') as flujo: 
                            for i in instance_servicios:
                                flujo.write (str(i.getserv_idServicio())+','+str(+i.getserv_cantidad())+','+str(+i.getserv_idTipoServicio())+','+str(i.getserv_idFactura())+'\n')
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
                                print(campos[2],' ', end='')
                                print(campo[3])
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

#reporteServicios()
#insertar()
#eliminar()
#modificar()
#consultartodo()