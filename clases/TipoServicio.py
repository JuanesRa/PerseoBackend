class tiposervicio():
    def __init__ (tise_idTipoServicio, tise_tipo, tise_precio):
        self.__tise_idTipoServicio=tise_idTipoServicio
        self.__tise_tipo=tise_tipo
        self.__tise_precio=tise_precio

    def getDatosTipoServicio(self):
        return self.__tise_idTipoServicio, self.__tise_tipo, self.__tise_precio
