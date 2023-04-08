import consultarreserva


def seleccion():
    print('id reserva--', 'cantidad habitacion--','numero de personas-- ','fecha ingreso--', 'fecha salida-- ','id usuario--','--numero habitacion')
    print(seleccion('tb_reserva','rese_idReserva','=','1'))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

import eliminarreserva

def eliminar():
    eliminar('tb_reserva','rese_idReserva',5)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------

import insertarreserva

def insertar():
    insertar('tb_reserva',5,5,5,'29-03-2023','30-03-2023',19999,909)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import mdificarreserva

def modificar():
    modificar('tb_reserva','rese_numPersonas',8,1)