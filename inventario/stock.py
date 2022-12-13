from inventario.producto import Producto

class Stock:
    
    def __init__(self) -> None:
        self.__productos: list[Producto] = []
        
    def __comprobar_producto(self, codigo: str) -> bool:
        return any(prod.codigo == codigo for prod in self.__productos)
        
    def agregar_producto(self, prod_a_agregar: Producto) -> None:
        if self.__comprobar_producto(prod_a_agregar.codigo):
            raise ValueError(f"El producto: {prod_a_agregar.codigo} ya existe")
        else:
            self.__productos.append(prod_a_agregar)
        
    def quitar_productos(self, prod_a_quitar: Producto) -> None:
        self.__productos.remove(prod_a_quitar)
        
    @property
    def productos(self) -> list[Producto]:
        return self.__productos
        