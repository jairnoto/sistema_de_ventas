class Cliente:
    def __init__(self, nombre, apellido, email,celular):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.celular = celular

    def mostrar_cliente(self):
        print(f"Nombre: {self.nombre} | Apellido: {self.apellido} | Email: {self.email} | Celular : {self.celular}")



class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_producto(self):
        print(f"Nombre: {self.nombre} | Precio: Bs {self.precio} | Cantidad: {self.cantidad}")

    

class Gestiondeventas:
    def __init__(self):
        self.clientes = []
        self.productos = []
        

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)


    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_clientes(self):
        print("Registro de clientes en la semana:")
        for cliente in self.clientes:
            cliente.mostrar_cliente()

    def mostrar_productos(self,):
        print("Lista de Productos:")
        for producto in self.productos:
            producto.mostrar_producto()

    def realizar_venta(self, nombre_producto, cantidad_vendida):
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                if producto.cantidad >= cantidad_vendida:
                    producto.cantidad -= cantidad_vendida
                    print(f"Venta realizada: {cantidad_vendida} {producto.nombre}(s)")
                else:
                    print(f"No hay suficiente stock de {producto.nombre}")
                return
        print(f"No se encontró el producto {nombre_producto}")
        
class Venta():
    def __init__(self, producto, cantidad, cliente):
        self.producto = producto
        self.cantidad = cantidad
        self.cliente = cliente

    def realizar_venta(self,):
        if self.producto.cantidad >= self.cantidad:
            self.producto.cantidad -= self.cantidad
            print(f"Venta realizada: {self.cantidad} {self.producto.nombre}(s) a {self.cliente.nombre} {self.cliente.apellido}")
        else:
            print(f"No hay suficiente stock de {self.producto.nombre} para realizar la venta")

class Inventario(Producto):
    def __init__(self, nombre,precio, cantidad):
        # Llamamos al constructor de la clase base (Producto)
        super().__init__(nombre, precio,cantidad)
      
    def mostrar_inventario(self):
        print(f"Inventario :")
        print(f"Nombre: {self.nombre} | Cantidad de Productos : {self.cantidad}")
       

# Resto del código sigue igual



# Ejemplo de uso
if __name__ == '__main__':
    sistema = Gestiondeventas()
    producto1 = Producto("Pelota", 60, 10)
    producto2 = Producto("Short", 40, 20)
    producto3 = Producto("Tenis", 120, 200)
    producto4 = Producto("Calzas", 30, 5)
    
    cliente1 = Cliente("Diego", "Lunda", "diegoLundaR@gmail.com", "67663309")
    cliente2 = Cliente("Alan", "Rodriguez","RodriguezR@gmail.com", "78505356")
    cliente3 = Cliente("Pepe", "Mamani", "Pepe20@gmail.com", "78902345")
    cliente4 = Cliente("Maria", "Lopez", "MariaVisnay@gmail.com", "70343535")
    
    inventario1 = Inventario("Pelota",0 ,10)
    inventario2 = Inventario("Short",0 ,20)
 
    
    sistema.agregar_cliente(cliente1)
    sistema.agregar_cliente(cliente2)
    sistema.agregar_cliente(cliente3)
    sistema.agregar_cliente(cliente4)
    sistema.mostrar_clientes()
    
    
    
    sistema.agregar_producto(producto1)
    sistema.agregar_producto(producto2)
    sistema.agregar_producto(producto3)
    sistema.agregar_producto(producto4)
    sistema.mostrar_productos()
   



    sistema.realizar_venta("Pelota", 10)
    sistema.realizar_venta("Short", 20)
    sistema.realizar_venta("Tenis", 200)
    sistema.realizar_venta("Calzas", 5)

    sistema.agregar_producto(inventario1)
    sistema.agregar_producto(inventario2)     
    for producto in sistema.productos:
        if isinstance(producto, Inventario):
            producto.mostrar_inventario()