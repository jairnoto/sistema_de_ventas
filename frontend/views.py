import streamlit as st
from backend.models import Cliente, Producto, Gestiondeventas, Venta, Inventario

# Crea una instancia de la clase Gestiondeventas
sistema = Gestiondeventas()

def mostrar_formulario_agregar_cliente():
    with st.form(key='cliente_form'):
        nombre = st.text_input(label='Nombre del Cliente')
        apellido = st.text_input(label='Apellido del Cliente')
        email = st.text_input(label='Email del Cliente')
        celular = st.text_input(label='Celular del Cliente')
        submit_button = st.form_submit_button(label='Agregar Cliente')

        if submit_button:
            cliente = Cliente(nombre, apellido, email, celular)
            sistema.agregar_cliente(cliente)
            st.success('Cliente agregado con éxito!')

def mostrar_formulario_agregar_producto():
    with st.form(key='producto_form'):
        nombre = st.text_input(label='Nombre del Producto')
        precio = st.number_input(label='Precio del Producto', min_value=0.0, format='%f')
        cantidad = st.number_input(label='Cantidad del Producto', min_value=0, format='%d')
        submit_button = st.form_submit_button(label='Agregar Producto')

        if submit_button:
            producto = Producto(nombre, precio, cantidad)
            sistema.agregar_producto(producto)
            st.success('Producto agregado con éxito!')

def mostrar_clientes():
    st.write("Clientes Registrados:")
    for cliente in sistema.clientes:
        cliente.mostrar_cliente()

def mostrar_productos():
    st.write("Productos Registrados:")
    for producto in sistema.productos:
        producto.mostrar_producto()

def run():
    st.title('Sistema de Gestión de Ventas')

    st.sidebar.title("Acciones")
    add_cliente = st.sidebar.checkbox("Agregar Cliente")
    add_producto = st.sidebar.checkbox("Agregar Producto")
    ver_clientes = st.sidebar.checkbox("Mostrar Clientes")
    ver_productos = st.sidebar.checkbox("Mostrar Productos")

    if add_cliente:
        mostrar_formulario_agregar_cliente()

    if add_producto:
        mostrar_formulario_agregar_producto()

    if ver_clientes:
        mostrar_clientes()

    if ver_productos:
        mostrar_productos()

# No olvides quitar el siguiente comentario si este archivo es el punto de entrada principal
# if _name_ == "_main_":
#     run()