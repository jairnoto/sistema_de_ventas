# models.py

import json

class Cliente:
    def __init__(self, nombre, apellido, email, celular):
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
        self.cargar_datos()

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)
        self.guardar_datos()

    def agregar_producto(self, producto):
        self.productos.append(producto)
        self.guardar_datos()

    def guardar_datos(self):
        datos_clientes = [{'nombre': c.nombre, 'apellido': c.apellido, 'email': c.email, 'celular': c.celular} for c in self.clientes]
        datos_productos = [{'nombre': p.nombre, 'precio': p.precio, 'cantidad': p.cantidad} for p in self.productos]
        datos = {'clientes': datos_clientes, 'productos': datos_productos}
        with open('datos.json', 'w') as archivo:
            json.dump(datos, archivo)

    def cargar_datos(self):
        try:
            with open('datos.json', 'r') as archivo:
                try:
                    datos_cargados = json.load(archivo)
                    self.clientes = [Cliente(c['nombre'], c['apellido'], c['email'], c['celular']) for c in datos_cargados.get('clientes', [])]
                    self.productos = [Producto(p['nombre'], p['precio'], p['cantidad']) for p in datos_cargados.get('productos', [])]
                except json.JSONDecodeError:
                    self.clientes = []
                    self.productos = []
        except FileNotFoundError:
            self.clientes = []
            self.productos = []


class Venta:
    def __init__(self, producto, cantidad, cliente):
        self.producto = producto
        self.cantidad = cantidad
        self.cliente = cliente

    # Resto del código permanece igual


class Inventario(Producto):
    def __init__(self, nombre, precio, cantidad):
        super().__init__(nombre, precio, cantidad)

    # Resto del código permanece igual
