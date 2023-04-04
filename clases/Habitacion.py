class habitacion:
    def __init__(self,nh,d,tipo,estado):
        self.numeroHab = nh
        self.descripcionHab = d
        self.tipoHab = tipo
        self.estadoHab=estado       
    #? getters/setters numeroHab    
    def getNumeroHab(self):
        return self.numeroHab
    def setNumeroHab(self,numeroHab):
        self.numeroHab = numeroHab
        
    #? getters/setters descripcionHab
    def getdescripcionHab(self):
        return self.descripcionHab
    def setdescripcionHab(self,descr):
        self.descripcionHab = descr
    #? getters/setter tipo habitacion
    def getTipoHab(self):
        return self.tipoHab
    def setTipoHab(self,tip):
        self.tipoHab=tip
    #? getters/setters
    def getEstado(self):
        return self.estado
    def setEstado(self, estado):
        self.estadoHab=estado    