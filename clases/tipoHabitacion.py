class tipoHab:
    def __init__(self,idth,tipo,precio):
        self.idTipoHab=idth 
        self.tipoHab = tipo
        self.precioHab = precio       
    #? getters/setters idTipoHab   
    def getidTipoHab(self):
        return self.idTipoHab
    def setidTipoHab(self,idtp):
        self.idTipoHab = idtp
    #? getters/setters tipoHab
    def gettipoHab(self):
        return self.tipoHab
    def settipoHab(self,tp):
        self.tipoHab = tp
    #? getters/setter precioHab
    def getprecioHab(self):
        return self.precioHab
    def setprecioHab(self,pre):
        self.precioHab=pre
