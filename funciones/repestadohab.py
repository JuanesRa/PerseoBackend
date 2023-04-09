import sqlite3
con=sqlite3.connect('db/Perseo.db')
micursor=con.cursor()

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
                    from crudEstadoHab import  modificarhab
                    sentencia=f"SELECT * FROM tb_estadoHabitacion"
                    lista=micursor.execute(sentencia)
                    ite=lista.fetchall()
                    #----------------------------------------------------
                    instance_estadohabitacion=[]
                    
                    dia_presente= d.date.today()
                    nombre_repor=str(input('Nombre del reporte a crear: '))
                    nombre_com=f'{nombre_repor}{dia_presente}'
                    if os.path.exists(f'reportes/{nombre_com}'):
                        raise FileExistsError
                    else:
                        for i in ite:
                            modificarhab.append(i)
                        
                        for campo in modificarhab:
                            objServicio=modificarhab(campo[0],campo[1])
                            instance_estadohabitacion.append(objServicio)

                        with open(f'reportes/{nombre_com}','a') as flujo: 
                            for i in instance_estadohabitacion:
                                flujo.write (str(i.getesha_idestadoHab())+','+str(+i.getesha_estado()))
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

reporteServicios()
