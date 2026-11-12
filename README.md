# NexusTech Store - Catálogo Tecnológico (Django MTV)

**Asignatura:** Desarrollo de Aplicaciones Web (IS093A)  
**Semana:** 11  
**Alumno:** Mauricio Paolo Vega Sanabria







##  Descripción del Proyecto
NexusTech Store es una aplicación web desarrollada con Django que implementa el patrón arquitectónico MTV (Model-Template-View). Consiste en un catálogo de productos tecnológicos con un diseño web moderno y responsivo (modo oscuro), que consume datos dinámicos desde una base de datos SQLite mediante el ORM de Django.

---

## 1. Configuración y Arquitectura MTV (20%)

### Estructura del Proyecto
El proyecto sigue la estructura estándar de Django, separando la configuración global (`config/`) de la lógica de la aplicación (`catalogo/`), e incluyendo carpetas para archivos estáticos y plantillas.

![Estructura del proyecto](Capturas/estructura.png)

### Configuración de `settings.py`
Se registró la aplicación `catalogo` y se configuró la ruta global para las plantillas (`templates/`).

![Configuración Settings](Capturas/settings.png)

### URLs y Routing
Se utilizó `include()` para modularizar las rutas y `name=` para desacoplar las vistas de los enlaces en las plantillas.

![Configuración URLs](Capturas/urls.png)

---

## 2. Vistas: FBV y CBV (20%)

### Vista Basada en Función (FBV) - `home`
Se encarga de renderizar la página de bienvenida con un contexto básico.

### Vista Basada en Clase (CBV) - `ProductoListView`
Se utilizó una vista genérica `ListView` para el catálogo, inyectando automáticamente el `object_list` y aplicando un QuerySet filtrado.

![Código de las Vistas](Capturas/vistas.png)

---

## 3. Modelos y ORM (25%)

### Modelo `Producto`
Se definió la clase `Producto` con los campos requeridos (nombre, precio, categoría, stock, imagen_url), aplicando tipos de datos adecuados (como `DecimalField` y `PositiveIntegerField`).

![Código del Modelo](Capturas/modelos.png)

### QuerySets utilizados
1. **QuerySet Principal (en `views.py`):** 
   `Producto.objects.filter(stock__gt=0).order_by('precio')`
   * **Propósito:** Filtra los productos que tengan stock disponible (mayor a 0) y los ordena de menor a mayor precio para mostrarlos en el catálogo.

2. **QuerySet en el Template (inyectado por la CBV):**
   `productos` (definido por `context_object_name`).
   * **Propósito:** Es el conjunto de datos iterable que la plantilla recorre para construir las tarjetas de los productos.

### Explicación de Lazy Evaluation (Evaluación Diferida)
Los QuerySets en Django son "perezosos" (lazy). Esto significa que **la consulta SQL a la base de datos no se ejecuta en el momento en que se declara el QuerySet en `views.py`**. Django simplemente "prepara" la consulta. La base de datos solo recibe la orden de ejecución (y devuelve los datos) cuando el resultado es estrictamente necesario, por ejemplo:
* Cuando el template ejecuta el bucle `{% for producto in productos %}`.
* Cuando en el código Python se convierte a lista (`list(queryset)`), se evalúa su longitud (`len()`) o se itera sobre él.
**Ventaja:** Esto ahorra recursos en el servidor, ya que si el QuerySet no llega a utilizarse, la base de datos nunca recibe la petición, optimizando el rendimiento.

---

## 4. Plantillas y Herencia (20%)

### Uso de Tags y Filtros en `catalogo.html`
Se implementó la herencia con `{% extends "base.html" %}`. Además, se utilizaron etiquetas de control de flujo como `{% for producto in productos %}` y `{% if producto.stock > 0 %}`. También se aplicaron filtros como `|title` para capitalizar nombres y `|floatformat:2` para mostrar el precio con dos decimales.

![Código Plantilla Catálogo](Capturas/plantilla_catalogo.png)

### Renderizado Final del Catálogo
Vista del catálogo funcionando, aplicando los estilos CSS, las imágenes y el filtro de productos con stock mayor a cero.

![Catálogo Renderizado](Capturas/catalogo1.png)
![Catálogo Renderizado](Capturas/catalogo2.png)

---

## 5. Validación Técnica y Administración (15%)

### Panel de Administración
Se registró el modelo en `admin.py` para gestionar los productos de forma visual. Se comprobó que `python manage.py check` se ejecuta sin errores.

![Panel de Administración](Capturas/admin.png)

---



## 6. Diagrama de flujo 
┌─────────────────────────────────────────────────────────┐
 │ 1. REQUEST (Cliente)                                    │
 │    El usuario entra a http://127.0.0.1:8000/catalogo/   │
 └────────────────────────────┬────────────────────────────┘
                              ▼
 ┌─────────────────────────────────────────────────────────┐
 │ 2. URLS (`config/urls.py` → `catalogo/urls.py`)         │
 │    Django intercepta y redirige al patrón correspondiente │
 └────────────────────────────┬────────────────────────────┘
                              ▼
 ┌─────────────────────────────────────────────────────────┐
 │ 3. VIEW (Lógica - `ProductoListView`)                   │
 │    Recibe la petición y solicita los datos necesarios   │
 └──────┬───────────────────────────────────────────▲──────┘
        │                                           │
        ▼ (Solicita datos)                          │ (Devuelve datos)
 ┌─────────────────────────┐                        │
 │ 4. MODEL (Datos / ORM)  ├────────────────────────┘
 │    Consulta SQL a SQLite│
 └─────────────────────────┘
        │
        ▼ (Pasa datos a la vista)
 ┌─────────────────────────────────────────────────────────┐
 │ 5. TEMPLATE (Presentación)                              │
 │    Renderiza el HTML dinámico (`catalogo.html`)         │
 └────────────────────────────┬────────────────────────────┘
                              ▼
 ┌─────────────────────────────────────────────────────────┐
 │ 6. RESPONSE (Respuesta)                                 │
 │    El servidor envía el documento HTML final al cliente │
 └─────────────────────────────────────────────────────────┘

---




##  Instalación y Ejecución Local
1. Clonar el repositorio.
2. Crear y activar un entorno virtual: `python -m venv venv` y `venv\Scripts\activate` (Windows).
3. Instalar Django: `pip install django`.
4. Aplicar migraciones: `python manage.py migrate`.
5. Ejecutar el servidor: `python manage.py runserver`.
6. Abrir en el navegador: `http://127.0.0.1:8000/`.