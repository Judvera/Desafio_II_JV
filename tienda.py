from producto import Producto

class Tienda:
    # Constructor clase Tienda
    def __init__(self, nombre, costo_delivery):
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        self.__productos = []

# Ingresa un producto
    def ingresar_producto(self, producto):
        for p in self.__productos:
            if p.get_nombre() == producto.get_nombre():
                p.set_stock(p.get_stock() + producto.get_stock())
                return
        self.__productos.append(producto)

# Listar productos de tienda
    def listar_productos(self):
        result = ""
        for producto in self.__productos:
            result += f"Nombre: {producto.get_nombre()}, Precio: ${producto.get_precio()}"
            if not isinstance(self, Restaurante):
                result += f", Stock: {producto.get_stock()}"
                if isinstance(self, Supermercado) and producto.get_stock() < 10:
                    result += " - Pocos productos disponibles"
                elif isinstance(self, Farmacia) and producto.get_precio() > 15000:
                    result += " - Envío gratis al solicitar este producto"
            result += "\n"
        return result
    
# Venta
    def realizar_venta(self, nombre_producto, cantidad):
        for producto in self.__productos:
            if producto.get_nombre() == nombre_producto:
                if isinstance(self, Farmacia) and cantidad > 3:
                    return
                if producto.get_stock() >= cantidad:
                    producto.set_stock(producto.get_stock() - cantidad)
                    return


class Restaurante(Tienda):
    pass


class Supermercado(Tienda):
    pass


class Farmacia(Tienda):
    pass
