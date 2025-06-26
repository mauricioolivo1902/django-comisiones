# Proyecto Académico: Sistema de Ventas y Comisiones con Django (MVC)

Este proyecto es una aplicación web desarrollada con el framework Django, que sigue el patrón de diseño MTV (Modelo-Template-Vista), una variante del clásico MVC. El sistema permite gestionar vendedores, reglas de comisión y ventas. Su funcionalidad principal es filtrar las ventas por un rango de fechas y calcular automáticamente la comisión correspondiente para cada una.

## Video Explicativo

https://www.youtube.com/watch?v=ps5crjXpq4g

## Repositorio en GitHub

El código fuente completo de este proyecto está disponible en el siguiente repositorio:

* **Enlace a GitHub:** https://github.com/mauricioolivo1902/django-comisiones

## Proyecto en Vivo (Deploy)

La aplicación está desplegada en PythonAnywhere y se puede probar en el siguiente enlace:

* **Enlace al Proyecto:** [http://MauricioOlivo.pythonanywhere.com/](http://MauricioOlivo.pythonanywhere.com/)

## Recursos y Documentación (Patrón MVC en Django)

Para el desarrollo de este proyecto y el aprendizaje del patrón MTV de Django, se utilizaron los siguientes recursos:

* **Documentación Oficial de Django:** La fuente principal y más fiable de información.
    * [Escribiendo tu primera aplicación con Django](https://docs.djangoproject.com/es/4.2/intro/tutorial01/)
    * [Documentación sobre Modelos](https://docs.djangoproject.com/es/4.2/topics/db/models/)
    * [Documentación sobre Vistas y Templates](https://docs.djangoproject.com/es/4.2/topics/http/views/)

* **Videos de Aprendizaje Recomendados:**
    * [Serie de Tutoriales de Django por Corey Schafer (Inglés)](https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p): Una de las mejores series de videos para aprender Django desde las bases hasta temas avanzados. (En este caso fue utilizado hasta el video 13)

## Cómo Ejecutar el Proyecto Localmente

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/mauricioolivo1902/django-comisiones.git](https://github.com/mauricioolivo1902/django-comisiones.git)
    cd django-comisiones
    ```
2.  **Crear y activar un entorno virtual:**
    ```bash
    # En Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```
3.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Aplicar migraciones y crear un superusuario:**
    ```bash
    python manage.py migrate
    python manage.py createsuperuser
    ```
5.  **Ejecutar el servidor:**
    ```bash
    python manage.py runserver
    ```
    Accede a `http://127.0.0.1:8000/` para ver la app y a `http://127.0.0.1:8000/admin/` para gestionar los datos.

## Información de Contacto

* **Estudiante:** Mauricio Olivo
* **Email Institucional:** esteban.olivo@udla.edu.ec
* **Email Personal:** mauricioolivo1902@gmail.com