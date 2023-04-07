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


#createUsuario()
#readUsuario()
#updateUsuario()
#deleteUsuario()