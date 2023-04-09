import sqlite3

conexion = sqlite3.connect("db/Perseo.db")
curstius = conexion.cursor()

except_ValueError = 'ERROR Intenta ingresar un valor no soportado por el sistema'
except_sqlite = 'ERROR!! Algún ID ingresado es incorrecto'


def createTipoUsuario():
    try:
        idtu = int(input('Ingrese el ID del tipo de usuario a crear\n'))
        tipo = str(input('Ingrese el tipo de usuario a crear '))
        sentencia = f"INSERT INTO tb_tipoUsuario VALUES ('{idtu}','{tipo}')"
        curstius.execute(sentencia)
        conexion.commit()
        print('Registro Creado!!!!')
    except ValueError:
        print(except_ValueError)
        createTipoUsuario()
    except sqlite3.IntegrityError:
        print(except_sqlite)
        createTipoUsuario()


def readTipoUsuario():
    sentencia = f'SELECT * FROM tb_tipoUsuario'
    lista = curstius.execute(sentencia)
    ite = lista.fetchall()
    print('Hay', len(ite),'tipo de usuario en el sistema. Se muestran a continuación: \n')
    for i in ite:
        print(i[0], '', end='')
        print(i[1], '\n', end='')


def updateTipoUsuario():
    while True:
        print('¿Que desea actualizar?\n 1 - ID tipo usuario\n 2 - Tipo\n 0 - Salir')
        ctrl = str(input('Seleccione una opción: '))
        if ctrl == '0':
            break
        else:
            num = int(input('Ingrese el ID del tipo de usuario\n'))
            v = idTipoUsuario()
            if num in v:
                match ctrl:
                    case '0':
                        break
                    case '1':
                        dato = int(input('Ingrese el nuevo ID del tipo de usuario\n'))
                        sentencia = f"UPDATE tb_tipoUsuario SET tius_idTipo = '{dato}'WHERE tius_idTipo = '{num}'"
                        curstius.execute(sentencia)
                        conexion.commit()
                        print('Modificación Exitosa!!!!\n')
                    case '2':
                        dato = str(input('Ingrese el nuevo tipo de usuario\n'))
                        sentencia = f"UPDATE tb_tipoUsuario SET tius_tipo = '{dato}'WHERE tius_idTipo = '{num}'"
                        curstius.execute(sentencia)
                        conexion.commit()
                        print('Modificación Exitosa!!!!\n')
            else:
                raise sqlite3.IntegrityError


def deleteTipoUsuario():
    try:
        list_idtius= idTipoUsuario()
        dato=int(input('Ingrese el ID del tipo usuario que desea eliminar\n'))
        if dato in list_idtius:
            sentencia=f"DELETE FROM tb_tipoUsuario WHERE tius_idTipo = '{dato}'"
            curstius.execute(sentencia)
            conexion.commit()
            print('Eliminación Exitosa!')
        else:
            print('No existe el tipo usuario', dato)
            raise sqlite3.IntegrityError
    except ValueError:
        print(except_ValueError)
        deleteTipoUsuario()
    except sqlite3.IntegrityError:
        deleteTipoUsuario()


def idTipoUsuario():
    sentencia = f"SELECT TU.tius_idTipo FROM tb_tipoUsuario TU"
    lista = curstius.execute(sentencia)
    ite = lista.fetchall()
    list_idUsua = []
    for i in ite:
        list_idUsua.append(i[0])
    return list_idUsua


def reporteTipoUsuario():
    while True:
        print('Reporte tipo de usuario:\n 1-Crear reporte\n 2-Ver reporte\n 3-Eliminar reporte')
        ctrl=str(input('Seleccione una opción: '))
        match ctrl:
            case '0':
                break
            case '1':
                try:
                    import os
                    import datetime as d
                    from sys import path
                    path.append('../PerseoBackend/Clases')
                    from TipoUsuario import tipoUsuario
                    sentencia=f"SELECT * FROM tb_tipoUsuario"
                    lista=curstius.execute(sentencia)
                    ite=lista.fetchall()
                    #----------------------------------------------------
                    instance_TipoUsua=[]
                    TipoUsuarios=[]
                    dia_presente= d.date.today()
                    nombre_repor=str(input('Nombre del reporte a crear: '))
                    nombre_com=f'{nombre_repor}{dia_presente}'
                    if os.path.exists(f'reportes/{nombre_com}'):
                        raise FileExistsError
                    else:
                        for i in ite:
                            TipoUsuarios.append(i)
                        
                        for campo in TipoUsuarios:
                            objUsua=tipoUsuario(campo[0],campo[1])
                            instance_TipoUsua.append(objUsua)

                        with open(f'reportes/{nombre_com}','a') as flujo: 
                            for i in instance_TipoUsua:
                                flujo.write (str(i.getIdTipo())+','+str(i.getTipo())+'\n')
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


#createTipoUsuario()
#readTipoUsuario()
#updateTipoUsuario()
#deleteTipoUsuario()
#reporteTipoUsuario()