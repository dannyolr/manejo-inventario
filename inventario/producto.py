class Producto:
    def __init__(self, codigo: str, nombre: str, precio: float, cantidad: int) -> None:
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio
        self.__cantidad = cantidad
    
    @property    
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, n_codigo: str) -> None:
        self.__codigo = n_codigo
        
    @property    
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, n_nombre: str) -> None:
        self.__nombre = n_nombre
        
    @property    
    def precio(self):
        return self.__precio
    
    @precio.setter
    def precio(self, n_precio: float) -> None:
        self.__precio = n_precio
        
    @property    
    def cantidad(self):
        return self.__cantidad
    
    @cantidad.setter
    def cantidad(self, n_cantidad: int) -> None:
        self.__cantidad = n_cantidad
        
    def __str__(self) -> str:
        return f'(Codigo: {self.__codigo}, Nombre: {self.__nombre}, Precio: {self.__precio}, Cantidad: {self.__cantidad})'
    