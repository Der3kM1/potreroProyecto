# Flask Web App

Este proyecto es una aplicación web construida con Python y Flask que permite a los usuarios explorar cursos a través de una interfaz amigable. La aplicación consume una API de cursos y muestra los datos en tarjetas interactivas.

## Estructura del Proyecto

```
flask-web-app
├── src
│   ├── app.py                # Punto de entrada de la aplicación Flask
│   ├── views
│   │   ├── home.py           # Vista para la página de inicio
│   │   ├── courses.py        # Vista que consume la API de cursos
│   │   └── detail.py         # Vista para mostrar detalles de un curso
│   ├── static
│   │   ├── css
│   │   │   └── styles.css     # Estilos CSS para la aplicación
│   │   └── js
│   │       └── courses.js     # Código JavaScript para manipular el DOM
│   ├── templates
│   │   ├── base.html         # Plantilla base para las páginas
│   │   ├── home.html         # Plantilla para la vista de inicio
│   │   ├── courses.html      # Plantilla para mostrar cursos en tarjetas
│   │   └── detail.html       # Plantilla para mostrar detalles de un curso
│   └── firebase
│       └── firebase_config.py # Configuración para conectar a Firebase
├── requirements.txt           # Dependencias del proyecto
└── README.md                  # Documentación del proyecto
```

## Instalación

1. Clona el repositorio:
   ```
   git clone <URL_DEL_REPOSITORIO>
   cd flask-web-app
   ```

2. Crea un entorno virtual:
   ```
   python -m venv venv
   source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
   ```

3. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```

## Uso

1. Ejecuta la aplicación:
   ```
   python src/app.py
   ```

2. Abre tu navegador y visita `http://127.0.0.1:5000` para ver la página de inicio.

