import sqlite3
conex=sqlite3.connect('db/Perseo.db')
curshab=conex.cursor()
#--------------------------------------------------------------------------------------

except_ValueError='ERROR Intenta ingresar un valor no soportado por el sistema'
except_sqlite='ERROR!! Algún ID ingresado es incorrecto'


#----------------------------------------------------------------------------------------
def selecTH():
    sentencia=f"SELECT * FROM tb_tipoHabitacion"
    lista=curshab.execute(sentencia)
    ite=lista.fetchall()
    print('Existen estos', len(ite), 'tipos de habitaciones y son: \n')
    for i in ite:
        print(i[0] ,'', end='')
        print(i[1] ,'', end='')
        print(i[2])
        print('_'*20)
        


def updateTH():
    try:
         while True:
            print('Que le quieres actualizar:\n 1-Número Tipo habitación\n 2-Tipo habitación\n 3-Precio:')
            ctrl=str(input('Que opción eliges: '))
            if ctrl == '0':
                break
            else:
                num=int(input('Número del tipo habitación a actualizar: '))
                v=id_tipoHab()
                if num in v:
                    match ctrl:
                        case '0':
                            break                  
            
                        case '1':
                            dato=int(input('Nuevo número de tipo habitación: '))
                            sentencia=f"UPDATE tb_tipoHabitacion SET tiha_idTipoHab='{dato}'WHERE tiha_idTipoHab='{num}'"
                            curshab.execute(sentencia)
                            conex.commit()
                            print('Modificación Exitosa!!!!\n')
                        case '2':
                            dato=str(input('Nuevo tipo de habitación: '))
                            sentencia=f"UPDATE tb_tipoHabitacion SET tiha_tipo='{dato}'WHERE tiha_idTipoHab='{num}'"
                            curshab.execute(sentencia)
                            conex.commit()
                            print('Modificación Exitosa!!!!\n')
                            
                        case '3':
                            dato=int(input('Nueva precio del tipo habitación: '))
                            sentencia=f"UPDATE tb_tipoHabitacion SET tiha_precio='{dato}'WHERE tiha_idTipoHab='{num}'"
                            curshab.execute(sentencia)
                            conex.commit()
                            print('Modificación Exitosa!!!!\n')
                            
                else:
                    raise sqlite3.IntegrityError
                
    except ValueError:
        print(except_ValueError)
        updateTH()
    except sqlite3.IntegrityError:
        print(except_sqlite)
        updateTH()



def deleteTH():
    try:
        list_TipoHab=id_tipoHab()
        dato=int(input('Número del tipo de habitación que quiere eliminar: '))
        if dato in list_TipoHab:
            sentencia=f"DELETE FROM tb_tipoHabitacion WHERE tiha_idTipoHab='{dato}'"
            curshab.execute(sentencia)
            conex.commit()
            print('Eliminación Exitosa!!!!')
        else:
            print('El id tipo habitación',dato,'No existe' )
            raise sqlite3.IntegrityError
    except ValueError:
        print(except_ValueError)
        deleteTH()
    except sqlite3.IntegrityError:
        print(except_sqlite)
        deleteTH()


def insertTH():
    try:
        idTH=int(input('Ingrese el ID del tipo de habitación: '))
        tpTH=str(input('Tipo de habitación: '))
        preTH=int(input('Precio del tipo de habitación: '))
        
        sentencia=f"INSERT INTO tb_tipoHabitacion VALUES ('{idTH}','{tpTH}',{preTH})"
        curshab.execute(sentencia)
        conex.commit()
        print('Registro Creado!!!!')
    except ValueError:
        print(except_ValueError)
        insertTH()
    except sqlite3.IntegrityError:
        print(except_sqlite)
        insertTH()


def id_tipoHab():
    sentencia=f"SELECT * FROM tb_tipoHabitacion"
    lista=curshab.execute(sentencia)
    ite=lista.fetchall()
    list_tipoHab=[]
    for i in ite:
        list_tipoHab.append(i[0])
    return list_tipoHab



def reporteTipoHab():
    while True:
        print('Reporte Tipo Habitación:\n 1-Crear reporte\n 2-Ver reporte\n 3-Eliminar reporte')
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
                    from tipoHabitacion import  tipoHab 
                    sentencia=f"SELECT * FROM tb_tipoHabitacion"
                    lista=curshab.execute(sentencia)
                    ite=lista.fetchall()
                    #----------------------------------------------------
                    instance_tipoHab=[]
                    tipo_habitacion=[]
                    dia_presente= d.date.today()
                    nombre_repor=str(input('Nombre del reporte a crear: '))
                    nombre_com=f'{nombre_repor}{dia_presente}'
                    if os.path.exists(f'reportes/{nombre_com}'):
                        raise FileExistsError
                    else:
                        for i in ite:
                            tipo_habitacion.append(i)
                        
                        for campo in tipo_habitacion:
                            objTipoHab=tipoHab(campo[0],campo[1],campo[2])
                            instance_tipoHab.append(objTipoHab)

                        with open(f'reportes/{nombre_com}','a') as flujo: 
                            for i in instance_tipoHab:
                                flujo.write (str(i.getidTipoHab())+','+i.gettipoHab()+','+str(i.getprecioHab())+'\n')
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
                                print(float(campos[2]))
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
                
            

    
#insertTH() 
#deleteTH()
#updateTH()
#selecTH()
#  reporteTipoHab()
