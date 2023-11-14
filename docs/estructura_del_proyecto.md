# Estructura del Proyecto de Sistema de Ventas

## Organización de Archivos y Carpetas
```
sistema_ventas/
│
├── app.py              # Archivo principal de la aplicación.
├── README.md           # Documentación del proyecto.
├── requirements.txt    # Dependencias del proyecto.
│
├── frontend/           # Carpeta para los archivos de Streamlit (Frontend).
│   └── views.py        # Vistas de Streamlit para la interfaz de usuario.
│
├── backend/            # Carpeta para la lógica del negocio (Backend).
│   ├── models.py       # Definiciones de las clases Cliente, Producto, etc.
│   └── utils.py        # Funciones útiles y auxiliares.
│
├── data/               # Carpeta para almacenar datos (si es necesario).
│   ├── clientes.json   # Datos de ejemplo para clientes.
│   └── productos.json  # Datos de ejemplo para productos.
│
└── tests/              # Carpeta para pruebas unitarias.
    ├── test_models.py  # Pruebas para los modelos.
    └── test_utils.py   # Pruebas para las funciones auxiliares.

```


## Descripción de la Estructura
- **app.py**: Archivo principal que ejecuta la aplicación.
- **README.md**: Documentación del proyecto.
- **requirements.txt**: Lista de dependencias del proyecto.

### Frontend
- **frontend/views.py**: Define las vistas de la interfaz de usuario de Streamlit.

### Backend
- **backend/models.py**: Contiene las clases del modelo de negocio.
- **backend/utils.py**: Funciones auxiliares y utilitarias.

### Datos
- **data/clientes.json**: Datos de clientes (ejemplo).
- **data/productos.json**: Datos de productos (ejemplo).

### Pruebas
- **tests/test_models.py**: Pruebas unitarias para los modelos.
- **tests/test_utils.py**: Pruebas unitarias para las funciones auxiliares.
