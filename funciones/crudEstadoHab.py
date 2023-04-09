import consultarestadohab
def consuhab():
    print(consuhab('tb_estadoHabitacion','esha_idEstadoHab','=','3'))

#----------------------------------------------------------------------------------------------------------------

import eliminarhabitacion

def eliminar():
    eliminar('tb_estadoHabitacion','esha_idestadoHab','3')
#-----------------------------------------------------------------------------------------------------------------------------

import insertarhabitacion
def insertarhab():
    insertarhab('tb_estadoHabitacion','4','ocupada')

#---------------------------------------------------------------------------------------------------------------------------

import modificarestadohab

def modificarhab():
    modificarhab('tb_estadoHabitacion','esha_idEstadoHab','ocupada',1)