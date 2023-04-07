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


#createTipoUsuario()
#readTipoUsuario()
#updateTipoUsuario()
#deleteTipoUsuario()