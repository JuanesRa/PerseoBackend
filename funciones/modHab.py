import sqlite3 
conex=sqlite3.connect('db/Perseo.db')
curshab=conex.cursor()


def selecHab():
    sentencia=f"SELECT H.habi_idHabitacion, H.habi_descripción, TH.tiha_tipo, TH.tiha_precio, TE.esha_estado FROM tb_habitacion H INNER JOIN tb_tipoHabitacion TH ON H.habi_idTipoHab = TH.tiha_idTipoHab INNER JOIN tb_estadoHabitacion TE ON H.habi_idEstadoHab = TE.esha_idEstadoHab"# WHERE {campo}{operador}'{dato}'"
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
        campo=str(input('Ingrese el campo a actualizar: '))
        dato=input('Dato a actualizar: ')
        num=int(input('número de habitación a actualizar: '))
        sentencia=f"UPDATE tb_habitacion SET {campo}='{dato}'WHERE habi_idhabitacion='{num}'"
        curshab.execute(sentencia)
        conex.commit()
        print('Modificación Exitosa!!!!')
    except ValueError:
        print('ERROR Intenta ingresar un valor no soportado por el sistema')
        updatehab()
    except sqlite3.IntegrityError:
        print('ERROR!! El ID que intenta ingresar ya existe')
        updatehab()


def deletehab():
    try:
        dato=int(input('Número de la habitación que quiere eliminar: '))
        sentencia=f"DELETE FROM tb_habitacion WHERE habi_idHabitacion='{dato}'"
        curshab.execute(sentencia)
        conex.commit()
        print('Eliminación Exitosa!!!!')
    except ValueError:
        print('ERROR Intenta ingresar un valor no soportado por el sistema')
        deletehab()
    except sqlite3.IntegrityError:
        print('ERROR!! El ID que intenta ingresar ya existe')
        deletehab()


def inserthab():
    try:
        ids=int(input('Ingrese número de la habitación: '))
        dp=str(input('Escriba la descripción de la habitación: '))
        th=int(input('Ingrese el tipo de habitación: '))
        eh=int(input('Ingrese el estado de la habitación: '))
        sentencia=f"INSERT INTO tb_habitacion VALUES ('{ids}','{dp}',{th},{eh})"
        curshab.execute(sentencia)
        conex.commit()
        print('Registro Creado!!!!')
    except ValueError:
        print('ERROR Intenta ingresar un valor no soportado por el sistema')
        inserthab()
    except sqlite3.IntegrityError:
        print('ERROR!! El ID que intenta ingresar ya existe')
        inserthab()


#inserthab() 
#deletehab()
#updatehab()
#seleccion() 
