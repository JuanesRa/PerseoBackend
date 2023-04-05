class reservacion:
    def __init__(self,rese_idReserva,rese_canHab,rese_numPersonas,rese_fechaInicio,rese_fechaFin,rese_idUsuario,rese_idHabitacion):
        self.__rese_idReserva=rese_idReserva
        self.__rese_canHab=rese_canHab
        self.__rese_numPersonas=rese_numPersonas
        self.__rese_fechaInicio=rese_fechaInicio
        self.__rese_fechaFin=rese_fechaFin
        self.__rese_idUsuario=rese_idUsuario
        self.__rese_idHabitacion=rese_idHabitacion

    def getrese_idReserva(self):
        return self.__rese_idReserva
    def getrese_canHab(self):
        return self.__rese_canHab
    def getrese_numPersonas(self):
        return self.__rese_numPersonas
    def getrese_fechaInicio(self):
        return self.__rese_fechaInicio
    def getrese_fechaFin(self):
        return self.__rese_fechaFin
    def getrese_idUsuairo(self):
        return self.__rese_idUsuario
    def getrese_idHabitacion(self):
        return self.__rese_idHabitacion