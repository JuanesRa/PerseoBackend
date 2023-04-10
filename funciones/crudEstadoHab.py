import sqlite3

con = sqlite3.connect('db/Perseo.db')
micursor = con.cursor()

def consuhab(tabla, campo, operador, dato):
    sentencia = f"SELECT * FROM {tabla} WHERE {campo}{operador}'{dato}'"
    #print(sentencia)
    lista = micursor.execute(sentencia)
    return lista.fetchall()

def eliminar(tabla, campo, dato):
    sentencia = f"DELETE FROM {tabla} WHERE {campo}='{dato}'"
    micursor.execute(sentencia)
    con.commit()
    print('Eliminación Exitosa!!!!')

def insertarhab(tabla, idhabi, estado):
    sentencia = f"INSERT INTO {tabla} VALUES ('{idhabi}','{estado}')"
    micursor.execute(sentencia)
    con.commit()
    print('Registro Creado!!!!')

def modificarhab(tabla, campo, dato, id):
    sentencia = f"UPDATE {tabla} SET {campo}='{dato}' WHERE id={id}"
    micursor.execute(sentencia)
    con.commit()
    print('Modificación Exitosa!!!!')

def menuEstadoHab():
    while True:
        print("\nMenú de servicios\n")
        print("1. Consultar estado de la habitación por ID")
        print("2. Eliminar una habitación o su estado")
        print("3. Agregar una habitación y su estado")
        print("4. Modificar el estado de una habitación")
        print("5. Salir")
    
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            tabla = 'tb_estadoHabitacion'
            campo = 'esha_idEstadoHab'
            operador = '='
            dato = input("Introduzca el ID de la habitación a consultar: ")
            resultado = consuhab(tabla, campo, operador, dato)
            print(resultado)
        elif opcion == "2":
            tabla = 'tb_estadoHabitacion'
            campo = 'esha_idestadoHab'
            dato = input("Introduzca el ID de la habitación o estado a eliminar: ")
            eliminar(tabla, campo, dato)
        elif opcion == "3":
            tabla = 'tb_estadoHabitacion'
            idhabi = input("Introduzca el ID de la habitación a agregar: ")
            estado = input("Introduzca el estado de la habitación a agregar: ")
            insertarhab(tabla, idhabi, estado)
        elif opcion == "4":
            tabla = 'tb_estadoHabitacion'
            campo = 'esha_idEstadoHab'
            dato = input("Introduzca el nuevo estado de la habitación: ")
            id = input("Introduzca el ID de la habitación a modificar: ")
            modificarhab(tabla, campo, dato, id)
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción del menú.")

def reporteEstadoHab():
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

#reporteServicios()


# en esta parte se puede modificar el estado de la habitacion, puede pasar de estar ocupada a disponible 

#consuhab()
#eliminar()
#insertarhab()
# modificarhab()
