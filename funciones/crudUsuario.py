import sqlite3

conexion = sqlite3.connect("db/Perseo.db")
cursusua = conexion.cursor()

except_ValueError='ERROR Intenta ingresar un valor no soportado por el sistema'
except_sqlite='ERROR!! Algún ID ingresado es incorrecto'


def createUsuario():
    try:
        id = int(input('Ingrese el número de identificación del usuario a crear\n'))
        nombre = str(input('Ingrese el nombre del usuario a crear\n'))
        apellido = str(input('Ingrese el apellido del usuario a crear\n'))
        email = str(input('Ingrese el correo electrónico del usuario a crear\n'))
        telefono = str(input('Ingrese el teléfono del usuario a crear\n'))
        direccion = str(input('Ingrese la dirección del usuario a crear\n'))
        password = str(input('Ingrese la contraseña del usuario a crear\n'))
        idTipoUsario = int(input('Ingrese el ID del tipo de usuario a crear\n'))
        sentencia = f"INSERT INTO tb_usuario VALUES ('{id}','{nombre}','{apellido}','{email}','{telefono}','{direccion}','{password}','{idTipoUsario}')"
        cursusua.execute(sentencia)
        conexion.commit()
        print('Registro Creado!')
    except ValueError:
        print(except_ValueError)
        createUsuario()
    except sqlite3.IntegrityError:
        print(except_sqlite)
        createUsuario()


def readUsuario():
    sentencia = f"SELECT TU.tius_tipo ,U.usua_idUsuario ,U.usua_nombre, U.usua_apellido, U.usua_email, U.usua_direccion FROM tb_usuario U INNER JOIN tb_tipoUsuario TU ON U.usua_idTipoUsuario = TU.tius_idTipo"
    lista = cursusua.execute(sentencia)
    ite = lista.fetchall()
    print('Hay', len(ite), 'Usuarios en el sistema. Se muestran a continuación: \n')
    for i in ite:
        print(i[0] ,'-', end=' ')
        print(i[1] ,'-', end=' ')
        print(i[2] ,'-', end=' ')
        print(i[3] ,'-', end=' ')
        print(i[4] ,'-', end=' ')
        print(i[5])
        print('_'*90)


def updateUsuario():
    try: 
        while True:
            print('¿Que desea actualizar?\n 1 - Número de identificación\n 2 - Nombre\n 3 - Apellido\n 4 - Correo electrónico\n 5 - Teléfono\n 6 - Dirección\n 7 - Contraseña\n 8 - Tipo de Usuario\n 0 - Salir')
            ctrl=str(input('Seleccione una opción: '))
            if ctrl == '0':
                break
            else:
                num=int(input('Ingrese su número de identificación\n'))
                v=idUsuario()
                if num in v:
                    match ctrl:
                        case '0':
                            break                  
            
                        case '1':
                            dato=input('Ingrese el nuevo número de identificación\n')
                            sentencia=f"UPDATE tb_usuario SET usua_idUsuario='{dato}'WHERE usua_idUsuario='{num}'"
                            cursusua.execute(sentencia)
                            conexion.commit()
                            print('Modificación Exitosa!\n')

                        case '2':
                            dato=input('Ingrese el nuevo nombre\n')
                            sentencia=f"UPDATE tb_usuario SET usua_nombre='{dato}'WHERE usua_idUsuario='{num}'"
                            cursusua.execute(sentencia)
                            conexion.commit()
                            print('Modificación Exitosa!\n')

                        case '3':
                            dato=input('Ingrese el nuevo apellido\n')
                            sentencia=f"UPDATE tb_usuario SET usua_apellido='{dato}'WHERE usua_idUsuario='{num}'"
                            cursusua.execute(sentencia)
                            conexion.commit()
                            print('Modificación Exitosa!\n')

                        case '4':
                            dato=input('Ingrese el nuevo correo electrónico\n')
                            sentencia=f"UPDATE tb_usuario SET usua_email='{dato}'WHERE usua_idUsuario='{num}'"
                            cursusua.execute(sentencia)
                            conexion.commit()
                            print('Modificación Exitosa!\n')

                        case '5':
                            dato=input('Ingrese el nuevo teléfono\n')
                            sentencia=f"UPDATE tb_usuario SET usua_telefono='{dato}'WHERE usua_idUsuario='{num}'"
                            cursusua.execute(sentencia)
                            conexion.commit()
                            print('Modificación Exitosa!\n')

                        case '6':
                            dato=input('Ingrese la nueva dirección\n')
                            sentencia=f"UPDATE tb_usuario SET usua_dirección='{dato}'WHERE usua_idUsuario='{num}'"
                            cursusua.execute(sentencia)
                            conexion.commit()
                            print('Modificación Exitosa!\n')

                        case '7':
                            dato=input('Ingrese la nueva contraseña\n')
                            sentencia=f"UPDATE tb_usuario SET usua_pass='{dato}'WHERE usua_idUsuario='{num}'"
                            cursusua.execute(sentencia)
                            conexion.commit()
                            print('Modificación Exitosa!\n')
                        
                        case '8':
                            from sys import path
                            path.append('../PerseoBackend/funciones')
                            import crudTipoUsuario as tu
                            list_tipoUsuario= tu.idTipoUsuario()
                            dato=int(input('Ingrese el ID del nuevo tipo de usuario\n'))
                            if dato in list_tipoUsuario:
                                sentencia=f"UPDATE tb_usuario SET usua_idTipoUsuario='{dato}'WHERE usua_idUsuario='{num}'"
                                cursusua.execute(sentencia)
                                conexion.commit()
                                print('Modificación Exitosa!\n')
                            else:
                                raise sqlite3.IntegrityError
                else:
                    print('El usuario con número de identificación', num, 'no existe')
    except ValueError:
        print(except_ValueError)
        updateUsuario()
    except sqlite3.IntegrityError:
        print(except_sqlite)
        updateUsuario()


def deleteUsuario():
    try:
        list_idUs= idUsuario()
        dato=int(input('Ingrese el ID del tipo usuario que desea eliminar\n'))
        if dato in list_idUs:
            sentencia=f"DELETE FROM tb_usuario WHERE usua_idUsuario = '{dato}'"
            cursusua.execute(sentencia)
            conexion.commit()
            print('Eliminación Exitosa!')
        else:
            print('No existe el usuario', dato)
            raise sqlite3.IntegrityError
    except ValueError:
        print(except_ValueError)
        deleteUsuario()
    except sqlite3.IntegrityError:
        deleteUsuario()


def idUsuario():
    sentencia = f"SELECT U.usua_idUsuario FROM tb_usuario U"
    lista=cursusua.execute(sentencia)
    ite=lista.fetchall()
    list_idUsua=[]
    for i in ite:
        list_idUsua.append(i[0])
    return list_idUsua


def reporteUsuario():
    while True:
        print('Reporte Usuario:\n 1-Crear reporte\n 2-Ver reporte\n 3-Eliminar reporte')
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
                    from Usuario import usuario
                    sentencia=f"SELECT U.usua_idUsuario ,U.usua_nombre, U.usua_apellido, U.usua_email, U.usua_direccion, U.usua_telefono, U.usua_pass, TU.tius_tipo FROM tb_usuario U INNER JOIN tb_tipoUsuario TU ON U.usua_idTipoUsuario = TU.tius_idTipo"
                    lista=cursusua.execute(sentencia)
                    ite=lista.fetchall()
                    #----------------------------------------------------
                    instance_Usua=[]
                    usuarios=[]
                    dia_presente= d.date.today()
                    nombre_repor=str(input('Nombre del reporte a crear: '))
                    nombre_com=f'{nombre_repor}{dia_presente}'
                    if os.path.exists(f'reportes/{nombre_com}'):
                        raise FileExistsError
                    else:
                        for i in ite:
                            usuarios.append(i)
                        
                        for campo in usuarios:
                            objUsua=usuario(campo[0],campo[1],campo[2],campo[3],campo[4],campo[5],campo[6],campo[7])
                            instance_Usua.append(objUsua)

                        with open(f'reportes/{nombre_com}','a') as flujo: 
                            for i in instance_Usua:
                                flujo.write (str(i.getId())+','+str(i.getNombre())+','+str(i.getApellido())+','+str(i.getEmail())+','+str(i.getTelefono())+','+str(i.getDireccion())+','+str(i.getPassword())+','+str(i.getTipoUsuario())+'\n')
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

#createUsuario()
#readUsuario()
#updateUsuario()
#deleteUsuario()
#reporteUsuario()