import sqlite3 
conex=sqlite3.connect('db/Perseo.db')
curshab=conex.cursor()
#Importa el módulo tipo de habitación


except_ValueError='ERROR Intenta ingresar un valor no soportado por el sistema'
except_sqlite='ERROR!! Algún ID ingresado es incorrecto'
def selecHab():
    sentencia=f"SELECT H.habi_idHabitacion, H.habi_descripción, TH.tiha_tipo, TH.tiha_precio, TE.esha_estado FROM tb_habitacion H INNER JOIN tb_tipoHabitacion TH ON H.habi_idTipoHab = TH.tiha_idTipoHab INNER JOIN tb_estadoHabitacion TE ON H.habi_idEstadoHab = TE.esha_idEstadoHab"
    lista=curshab.execute(sentencia)
    ite=lista.fetchall()
    print('Hay', len(ite), 'Habitaciones en el hotel y son: \n')
    for i in ite:
        print(i[0] ,'', end='')
        print(i[1] ,'', end='')
        print(i[2] ,'', end='')
        print(i[3] ,'', end='')
        print(i[4])
        print('_'*90)
 

    

def updatehab():
    try:
        
        while True:
            print('Que le quieres actualizar:\n 1-Número habitación\n 2-Descripción\n 3-Tipo habitación\n 4-Estado habitación:')
            ctrl=str(input('Que opción eliges: '))
            if ctrl == '0':
                break
            else:
                num=int(input('Número de habitación a actualizar: '))
                v=id_Hab()
                if num in v:
                    match ctrl:
                        case '0':
                            break                  
            
                        case '1':
                            dato=int(input('Nuevo número de la habitación: '))
                            sentencia=f"UPDATE tb_habitacion SET habi_idHabitacion='{dato}'WHERE habi_idhabitacion='{num}'"
                            curshab.execute(sentencia)
                            conex.commit()
                            print('Modificación Exitosa!!!!\n')
                        case '2':
                            dato=str(input('Nueva descripción: '))
                            sentencia=f"UPDATE tb_habitacion SET habi_descripción='{dato}'WHERE habi_idhabitacion='{num}'"
                            curshab.execute(sentencia)
                            conex.commit()
                            print('Modificación Exitosa!!!!\n')
                            
                        case '3':
                            from sys import path
                            path.append('../PerseoBackend/funciones')
                            import crudTipoHabitacion as th
                            list_tipoHa= th.id_tipoHab()
                            dato=int(input('Nuevo tipo de habitación: '))
                            if dato in list_tipoHa:
                                sentencia=f"UPDATE tb_habitacion SET habi_idTipoHab='{dato}'WHERE habi_idhabitacion='{num}'"
                                curshab.execute(sentencia)
                                conex.commit()
                                print('Modificación Exitosa!!!!\n')
                            else:
                                raise sqlite3.IntegrityError
                        case '4':
                            list_estadoHab=id_EstHab()
                            dato=int(input('Nueva estado de habitación: '))
                            if dato in list_estadoHab:
                                sentencia=f"UPDATE tb_habitacion SET habi_idEstadoHab='{dato}'WHERE habi_idhabitacion='{num}'"
                                curshab.execute(sentencia)
                                conex.commit()
                                print('Modificación Exitosa!!!!\n')
            
                            else:
                                raise sqlite3.IntegrityError
                else:
                    print('La habitación', num, 'no existe')
    except ValueError:
        print(except_ValueError)
        updatehab()
    except sqlite3.IntegrityError:
        print(except_sqlite)
        updatehab()


def deletehab():
    try:
        list_hab= id_Hab()
        dato=int(input('Número de la habitación que quiere eliminar: '))
        if dato in list_hab:
            sentencia=f"DELETE FROM tb_habitacion WHERE habi_idHabitacion='{dato}'"
            curshab.execute(sentencia)
            conex.commit()
            print('Eliminación Exitosa!!!!')
        else:
            print('No existe la habitación', dato)
            raise sqlite3.IntegrityError
    except ValueError:
        print(except_ValueError)
        deletehab()
    except sqlite3.IntegrityError:
        deletehab()


def inserthab():
    try:
        from sys import path
        path.append('../PerseoBackend/funciones')
        import crudTipoHabitacion as th
        list_tipoHa= th.id_tipoHab()
        ids=int(input('Ingrese número de la habitación: '))
        dp=str(input('Escriba la descripción de la habitación: '))
        th=int(input('Ingrese el tipo de habitación: '))
        eh=int(input('Ingrese el estado de la habitación: '))
        if th in list_tipoHa:
            sentencia=f"INSERT INTO tb_habitacion VALUES ('{ids}','{dp}',{th},{eh})"
            curshab.execute(sentencia)
            conex.commit()
            print('Registro Creado!!!!')
        else:
            raise sqlite3.IntegrityError
    except ValueError:
        print(except_ValueError)
        inserthab()
    except sqlite3.IntegrityError:
        print(except_sqlite)
        inserthab()

def id_Hab():
    sentencia=f"SELECT H.habi_idHabitacion, H.habi_descripción, TH.tiha_tipo, TH.tiha_precio, TE.esha_estado FROM tb_habitacion H INNER JOIN tb_tipoHabitacion TH ON H.habi_idTipoHab = TH.tiha_idTipoHab INNER JOIN tb_estadoHabitacion TE ON H.habi_idEstadoHab = TE.esha_idEstadoHab"
    lista=curshab.execute(sentencia)
    ite=lista.fetchall()
    list_Hab=[]
    for i in ite:
        list_Hab.append(i[0])
    return list_Hab

def id_EstHab():
    sentencia=f"SELECT * FROM tb_estadoHabitacion"
    lista=curshab.execute(sentencia)
    ite=lista.fetchall()
    list_estHab=[]
    for i in ite:
        list_estHab.append(i[0])
    return list_estHab

def reporteHabit():
    while True:
        print('Reporte Habitación:\n 1-Crear reporte\n 2-Ver reporte\n 3-Eliminar reporte')
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
                    from Habitacion import  habitacion
                    sentencia=f"SELECT H.habi_idHabitacion, H.habi_descripción, TH.tiha_tipo, TE.esha_estado FROM tb_habitacion H INNER JOIN tb_tipoHabitacion TH ON H.habi_idTipoHab = TH.tiha_idTipoHab INNER JOIN tb_estadoHabitacion TE ON H.habi_idEstadoHab = TE.esha_idEstadoHab"
                    lista=curshab.execute(sentencia)
                    ite=lista.fetchall()
                    #----------------------------------------------------
                    instance_Habit=[]
                    habitaciones=[]
                    dia_presente= d.date.today()
                    nombre_repor=str(input('Nombre del reporte a crear: '))
                    nombre_com=f'{nombre_repor}{dia_presente}'
                    if os.path.exists(f'reportes/{nombre_com}'):
                        raise FileExistsError
                    else:
                        for i in ite:
                            habitaciones.append(i)
                        
                        for campo in habitaciones:
                            objHabit=habitacion(campo[0],campo[1],campo[2],campo[3])
                            instance_Habit.append(objHabit)

                        with open(f'reportes/{nombre_com}','a') as flujo: 
                            for i in instance_Habit:
                                flujo.write (str(i.getNumeroHab())+','+i.getdescripcionHab()+','+str(i.getTipoHab())+','+str(i.getEstadoHab())+'\n')
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
                                print(str(campos[2]),' ', end='')
                                print(str(campos[3]))
                               
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


#inserthab() 
#deletehab()
#updatehab()
#selecHab()
#reporteHabit() 



