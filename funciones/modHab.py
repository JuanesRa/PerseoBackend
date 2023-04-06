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
        from sys import path
        path.append('../PerseoBackend/funciones')
        import modTipoHab as th
        list_tipoHa= th.id_tipoHab()
        campo=str(input('Ingrese el campo a actualizar: '))
        dato=input('Dato a actualizar: ')
        num=int(input('número de habitación a actualizar: '))
        if campo=='habi_idTipoHab' and dato in list_tipoHa:
            sentencia=f"UPDATE tb_habitacion SET {campo}='{dato}'WHERE habi_idhabitacion='{num}'"
            curshab.execute(sentencia)
            conex.commit()
            print('Modificación Exitosa!!!!')
        elif campo=='habi_idEstadoHab':
            pass
        else:
            raise sqlite3.IntegrityError
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
        import modTipoHab as th
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


#inserthab() 
#deletehab()
updatehab()
selecHab() 
