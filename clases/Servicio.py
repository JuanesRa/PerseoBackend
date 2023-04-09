class servicio:
    def __init__ (self, idServicio,cantidad, idTipoServicio, idFactura):
        self.serv_idServicio=idServicio
        self.serv_cantidad=cantidad
        self.serv_idTipoServicio=idTipoServicio
        self.serv_idFactura=idFactura

    def getserv_idServicio(self):
        return self.serv_idServicio
    def setserv_idServicio(self,serv_idServicio):
        self.serv_idServicio = idServicio
    def getserv_cantidad(self):
        return self.serv_cantidad
    def setserv_cantidad(self,serv_cantidad):
        self.serv_cantidad = cantidad
    def getserv_idTipoServicio(self):
        return self.serv_idTipoServicio
    def setserv_idTipoServicio(self,serv_idTipoServicio):
        self.serv_idTipoServicio = idTipoServicio
    def getserv_idFactura(self):
        return self.serv_idFactura
    def setserv_idFactura(self,serv_idFactura):
        self.serv_idFactura = idFactura

     