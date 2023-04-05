class servicio:
    def __init__ (self, serv_idServicio, serv_cantidad, serv_idTipoServicio, serv_idFactura):
        self.__serv_idServicio=serv_idServicio
        self.__serv_cantidad=serv_cantidad
        self.__serv_idTipoServicio=serv_idTipoServicio
        self.__serv_idFactura=serv_idFactura

    def getDatosServicio(self):
        return self.__serv_idServicio, self.__serv_cantidad, self.__serv_idTipoServicio, self.__serv_idFactura
        