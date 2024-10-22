Proyecto 2 - Práctica con Django: 'Gestor de Notas'

Objetivo:
Este proyecto tiene como objetivo desarrollar una aplicación en Django que permita gestionar notas para cada usuario autenticado. Cada usuario podrá crear, editar, ver y eliminar sus notas. El proyecto está personalizado con los apellidos de los integrantes del equipo, conforme a las instrucciones recibidas.

1. Configuración del Proyecto:

1.1 Nombre del Proyecto:
- `project_[Apellido1Apellido2]`: El proyecto de Django debe ser nombrado según los apellidos del equipo.

1.2 Nombre de la Aplicación:
- `notes_[NombreApellido1Apellido2]`: La aplicación se encargará de gestionar las notas de los usuarios autenticados.

2. Modelos:

Modelo `Note`:
Dentro de la aplicación `notes_[Apellido1Apellido2]`, se ha creado un modelo `Note` con los siguientes campos:

- `user`: Relación de clave foránea con el modelo `User`, con `on_delete=models.CASCADE` y `related_name='notes'`.
- `title`: `CharField` de hasta 50 caracteres, que representa el título de la nota.
- `content`: `TextField` que almacena el contenido de la nota.
- `creation_date`: `DateTimeField` que se genera automáticamente al crear la nota.

Método especial `__str__`:  
Este método retorna el título (`title`) de la nota.

3. Vistas y URLs:

Vistas Implementadas:
- Lista de notas: Muestra todas las notas existentes para el usuario autenticado.
- Detalle de nota: Muestra el contenido detallado de una nota específica.
- Crear nota: Proporciona un formulario para crear una nueva nota.
- Editar nota: Formulario para modificar una nota existente.
- Eliminar nota: Permite eliminar una nota seleccionada.

 URLs Configuradas:
En el archivo `urls.py` de `notes_[Apellido1Apellido2]`, se han configurado las siguientes rutas:

- Lista de notas: `''`
- Detalle de nota: `'<int:pk>/'`
- Creación de nota: `'new/'`
- Edición de nota: `'<int:pk>/edit/'`
- Eliminación de nota: `'<int:pk>/delete/'`

 4. Templates:

En la carpeta `templates/notes_[Apellido1Apellido2]`, se han creado las siguientes plantillas:

- note_list_[Apellido1Apellido2].html: Muestra la lista de notas del usuario autenticado.
- note_detail_[Apellido1Apellido2].html: Muestra el contenido detallado de una nota específica.
- note_edit_[Apellido1Apellido2].html: Formulario utilizado para crear y editar notas.

 5. Casos de Prueba:

Se han escrito los siguientes casos de prueba en el archivo `tests.py`:

- Creación de nota: Verifica la correcta creación de una nueva nota.
- Actualización de nota: Comprueba que los datos de una nota existente puedan ser actualizados.
- Visualización de detalles: Asegura que el contenido de una nota se pueda visualizar correctamente.
- Eliminación de nota: Verifica que una nota pueda ser eliminada correctamente.
- Carga de la lista de notas: Comprueba que la lista de notas para un usuario autenticado se cargue correctamente.

 6. Instrucciones adicionales:

 6.1 Actualización de `settings.py`:
- Añadir `notes_[Apellido1Apellido2]` a la lista de `INSTALLED_APPS`.
- Configurar las rutas de autenticación para redirigir a los usuarios a las páginas correspondientes.

 6.2 Migraciones:
Ejecutar los siguientes comandos para aplicar las migraciones de la base de datos:

```bash
python manage.py makemigrations
python manage.py migrate
```

 6.3 Ejecutar el servidor:
Para ejecutar el servidor de desarrollo, utilizar el comando:

```bash
python manage.py runserver
```

 7. Requisitos Previos:
- Python 3.x
- Django 3.x o superior
- Base de datos configurada (SQLite por defecto en Django)
