import sqlite3
from sys import path
path.append('../PerseoBackend/funciones')

conexion = sqlite3.connect("db/Perseo.db")
cursorr = conexion.cursor()

import crudHabitacion as h
import crudTipoUsuario as tu
import crudUsuario as u
import crudtiposervicio as ts
import crudservicio as s
import crudTipoHabitacion as th
import crudEstadoHab as eh
import crudReserva as r


def menu():
    ndco = input('Ingrese su número de documento: ')
    sentencia = f"SELECT usua_idTipoUsuario FROM tb_usuario WHERE usua_idUsuario = '{ndco}'"
    lista = cursorr.execute(sentencia)
    ite = lista.fetchall()
    if len(ite) > 0:
        valor = ite[0][0]

        if valor == 1:
            while True:
                print('\nHOTEL PERSEO\n \nMenu Admin\n\n 1-Consultar\n 2-Insertar\n 3-Eliminar\n 4-Actualizar\n 5-Reportes\n 0-Salir')
                ctrl = str(input('Seleccione una opción: '))
                print()
                match ctrl:
                    case '0':
                        break
                    case '1':
                        while True:
                            print('\nCONSULTAR:\n\n 1-Habitación\n 2-Tipo de Habitación\n 3-Usuarios\n 4-Tipo de usuarios\n 5-Servicios\n 6-Tipo Servicios\n 7-Reservas\n 8-Estado de habitacion\n 0-Salir')
                            ctrl = str(input('Seleccione una opción: '))
                            print()
                            match ctrl:
                                case '0':
                                    break
                                case '1':
                                    h.selecHab()
                                    print()
                                case '2':
                                    th.selecTH()
                                    print()
                                case '3':
                                    u.readUsuario()
                                    print()
                                case '4':
                                    tu.readTipoUsuario()
                                    print
                                case '5':
                                    s.consultartodo()
                                    print()
                                case '6':
                                    ts.consultartipo()
                                    print()
                                case '7':
                                    r.seleccion()
                                    print()
                                case '8':
                                    eh.menuEstadoHab()
                                    print()
                                case _:
                                    print('Esta opción no existe')

                    case '2':
                        while True:
                            print('\nINSERTAR:\n\n 1-Habitación\n 2-Tipo de Habitación\n 3-Usuarios\n 4-Tipo de usuarios\n 5-Servicios\n 6-Tipo Servicios\n 7-Reservas\n 8-Estado de habitacion\n 0-Salir')
                            ctrl = str(input('Seleccione una opción: '))
                            print()
                            match ctrl:
                                case '0':
                                    break
                                case '1':
                                    h.inserthab()
                                    print()
                                case '2':
                                    th.insertTH()
                                    print()
                                case '3':
                                    u.createUsuario()
                                    print()
                                case '4':
                                    tu.createTipoUsuario()
                                    print()
                                case '5':
                                    s.insertar()
                                    print()
                                case '6':
                                    ts.insertartipo()
                                    print()
                                case '7':
                                    r.insertarre()
                                    print()
                                case '8':
                                    eh.menuEstadoHab()
                                    print()
                                case _:
                                    print('Esta opción no existe')
                    case '3':
                        while True:
                            print('\nELIMINAR:\n\n 1-Habitación\n 2-Tipo de Habitación\n 3-Usuarios\n 4-Tipo de usuarios\n 5-Servicios\n 6-Tipo Servicios\n 7-Reservas\n 8-Estado de habitacion\n 0-Salir')
                            ctrl = str(input('Seleccione una opción: '))
                            print()
                            match ctrl:
                                case '0':
                                    break
                                case '1':
                                    h.deletehab()
                                    print()
                                case '2':
                                    th.deleteTH()
                                    print()
                                case '3':
                                    u.deleteUsuario()
                                    print()
                                case '4':
                                    tu.deleteTipoUsuario()
                                    print()
                                case '5':
                                    s.eliminar()
                                    print()
                                case '6':
                                    ts.eliminartipo()
                                    print()
                                case '7':
                                    r.eliminarre()
                                    print()
                                case '8':
                                    eh.menuEstadoHab()
                                    print()
                                case _:
                                    print('Esta opción no existe')

                    case '4':
                        while True:
                            print('\nACTUALIZAR:\n\n 1-Habitación\n 2-Tipo de Habitación\n 3-Usuarios\n 4-Tipo de usuarios\n 5-Servicios\n 6-Tipo Servicios\n 7-Reservas\n 8-Estado de habitacion\n 0-Salir')
                            ctrl = str(input('Seleccione una opción: '))
                            print()
                            match ctrl:
                                case '0':
                                    break
                                case '1':
                                    h.updatehab()
                                    print()
                                case '2':
                                    th.updateTH()
                                    print()
                                case '3':
                                    u.updateUsuario()
                                    print()
                                case '4':
                                    tu.updateTipoUsuario()
                                    print()
                                case '5':
                                    s.modificar()
                                    print()
                                case '6':
                                    ts.modificartipo()
                                    print()
                                case '7':
                                    r.modificarre()
                                    print()
                                case '8':
                                    eh.menuEstadoHab()
                                    print()
                                case _:
                                    print('Esta opción no existe')
                    case '5':
                        while True:
                            print('\nREPORTES:\n\n 1-Habitación\n 2-Tipo de Habitación\n 3-Usuarios\n 4-Tipo de usuarios\n 5-Servicios\n 6-Tipo Servicios\n 7-Reservas\n 8-Estado de habitacion\n 0-Salir')
                            ctrl = str(input('Seleccione una opción: '))
                            print()
                            match ctrl:
                                case '0':
                                    break
                                case '1':
                                    h.reporteHabit()
                                    print()
                                case '2':
                                    th.reporteTipoHab()
                                    print()
                                case '3':
                                    u.reporteUsuario()
                                    print()
                                case '4':
                                    tu.reporteTipoUsuario()
                                    print()
                                case '5':
                                    s.reporteServicios()
                                    print()
                                case '6':
                                    ts.reporteTipoServicio()
                                    print()
                                case '7':
                                    #Funcion David
                                    print()
                                case '8':
                                    eh.reporteEstadoHab()
                                    print()
                                case _:
                                    print('Esta opción no existe')
                    case _:
                        print('Esta opción no existe')
        else:
            print("No se encontraron resultados")
    
menu()