class TV:
    _numTV= 0
    def __init__(self, marca, estado:bool) -> None:
        self._marca=marca
        self._canal =1
        self._precio=500
        self._estado= estado
        self._volumen = 1
        self._control = None
        TV._numTV +=1

    @classmethod
    def getNumTV(cls)->int:
        return cls._numTV
    
    @classmethod
    def setNumTV(cls, numTV:int)-> None:
        cls._numTV=numTV
    
    def getMarca(self):
        return self._marca
    def setMarca(self, marca)-> None:
        self._marca= marca
    def getCanal(self)-> int:
        return self._canal
    def setCanal(self, canal:int):
        if self._estado and self._canal>= 1 and self._canal<=120:
            self._canal=canal
    def getPrecio(self)-> int:
        return self._precio
    def setPrecio(self, volumen:int):
        if self._estado and self._volumen>= 0 and self._volumen<=7:
            self._volumen= volumen
