class usuario:
    def __init__(self,id,nombre,apellido,mail,telefono,direccion,password,tipoUsuario):
        self.__id = id
        self.__nombre = nombre
        self.__apellido = apellido
        self.__mail = mail
        self.__telefono = telefono
        self.__direccion = direccion
        self.__password = password
        self.__tipoUsuario = tipoUsuario
        
    def getId(self):
        return self.__id
    
    def setId(self,id):
        self.__id = id
        
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self,nombre):
        self.__nombre = nombre
    
    def getApellido(self):
        return self.__apellido
    
    def setApellido(self,apellido):
        self.__apellido = apellido
    
    def getEmail(self):
        return self.__mail
    
    def setEmail(self,mail):
        self.__mail = mail
        
    def getTelefono(self):
        return self.__telefono
    
    def setTelefono(self,telefono):
        self.__telefono = telefono
        
    def getDireccion(self):
        return self.__direccion
    
    def setDireccion(self,direccion):
        self.__direccion = direccion
        
    def getPassword(self):
        return self.__password
    
    def setPassword(self,password):
        self.__password = password
        
    def getTipoUsuario(self):
        return self.__tipoUsuario
    
    def setTipoUsuario(self, tipoUsuario):
        self.__tipoUsuario = tipoUsuario