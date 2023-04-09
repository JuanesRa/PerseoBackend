import sqlite3
from sys import path
path.append('../PerseoBackend/funciones')

conexion = sqlite3.connect("db/Perseo.db")
cursorr = conexion.cursor()

import modHab as h
import crudTipoUsuario as tu
import crudUsuario as u
import crudtiposervicio as ts
import crudservicio as s
import modTipoHab as th


def menu():
    ndco = input('Ingrese su número de documento: ')
    sentencia = f"SELECT usua_idTipoUsuario FROM tb_usuario WHERE usua_idUsuario = {ndco}"
    r = cursorr.execute(sentencia)
    ite = r.fetchone()
    print(ite)


menu()