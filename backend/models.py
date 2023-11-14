# models.py

class Cliente:
    def _init_(self, nombre, apellido, email, celular):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.celular = celular

    def mostrar_cliente(self):
        print(f"Nombre: {self.nombre} | Apellido: {self.apellido} | Email: {self.email} | Celular : {self.celular}")


class Producto:
    def _init_(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_producto(self):
        print(f"Nombre: {self.nombre} | Precio: Bs {self.precio} | Cantidad: {self.cantidad}")


class Gestiondeventas:
    def _init_(self):
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

    def mostrar_productos(self):
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


class Venta:
    def _init_(self, producto, cantidad, cliente):
        self.producto = producto
        self.cantidad = cantidad
        self.cliente = cliente

    def realizar_venta(self):
        if self.producto.cantidad >= self.cantidad:
            self.producto.cantidad -= self.cantidad
            print(f"Venta realizada: {self.cantidad} {self.producto.nombre}(s) a {self.cliente.nombre} {self.cliente.apellido}")
        else:
            print(f"No hay suficiente stock de {self.producto.nombre} para realizar la venta")


class Inventario(Producto):
    def _init_(self, nombre, precio, cantidad):
        super()._init_(nombre, precio, cantidad)

    def mostrar_inventario(self):
        print(f"Inventario :")
        print(f"Nombre: {self.nombre} | Cantidad de Productos : {self.cantidad}")