import sqlite3 
conex=sqlite3.connect('db/Perseo.db')
curshab=conex.cursor()


def selecTH():
    sentencia=f"SELECT * FROM tb_tipoHabitacion"# WHERE {campo}{operador}'{dato}'"
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
        campo=str(input('Ingrese el campo a actualizar: '))
        dato=input('Dato a actualizar: ')
        num=int(input('ID del tipo de habitación a actualizar: '))
        sentencia=f"UPDATE tb_tipoHabitacion SET {campo}='{dato}'WHERE tiha_idTipoHab='{num}'"
        curshab.execute(sentencia)
        conex.commit()
        print('Modificación Exitosa!!!!')
    except ValueError:
        print('ERROR Intenta ingresar un valor no soportado por el sistema')
        updateTH()
    except sqlite3.IntegrityError:
        print('ERROR!! El ID que intenta ingresar ya existe')
        updateTH()



def deleteTH():
    try:
        dato=int(input('Número del tipo de habitación que quiere eliminar: '))
        sentencia=f"DELETE FROM tb_tipoHabitacion WHERE tiha_idTipoHab='{dato}'"
        curshab.execute(sentencia)
        conex.commit()
        print('Eliminación Exitosa!!!!')
    except ValueError:
        print('ERROR Intenta ingresar un valor no soportado por el sistema')
        deleteTH()
    except sqlite3.IntegrityError:
        print('ERROR!! El ID que intenta ingresar ya existe')
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
        print('ERROR Intenta ingresar un valor no soportado por el sistema')
        insertTH()
    except sqlite3.IntegrityError:
        print('ERROR!! El ID que intenta ingresar ya existe')
        insertTH()
    
#insertTH() 
#deleteTH()
#updateTH()
#selecTH()
