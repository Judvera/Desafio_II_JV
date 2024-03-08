# Clase
class Producto:
    # Constructor
    def __init__(self, nombre, precio, stock=0):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = max(stock, 0)

# Obtener nombre producto
    def get_nombre(self):
        return self.__nombre
    
# Obtener precio producto
    def get_precio(self):
        return self.__precio
    
# Obtener stock
    def get_stock(self):
        return self.__stock
    
# Actualiza stock
    def set_stock(self, nuevo_stock):
        self.__stock = max(nuevo_stock, 0)
