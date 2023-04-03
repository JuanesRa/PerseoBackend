class tipoUsuario:
    def __init__(self,idTipo,tipo):
        self.__idTipo = idTipo
        self.__tipo = tipo
        
    def getIdTipo(self):
        return self.__idTipo
    
    def setIdTipo(self,idTipo):
        self.__idTipo = idTipo
        
    def getTipo(self):
        self.__tipo
        
    def setTipo(self,tipo):
        self.__tipo = tipo