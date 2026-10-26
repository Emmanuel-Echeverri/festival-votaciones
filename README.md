# Sistema de votaciones – Festival de la Leyenda Vallenata

Proyecto Django (patrón MVT) + MySQL. Estructura: Edición → Categoría → Votación → Opción.

## Requisitos
- Python 3.10+
- MySQL Server 8 (o MariaDB)
- Windows: Microsoft C++ Build Tools solo si `mysqlclient` no instala con wheel

## Instalación
```
python -m venv venv
venv\Scripts\activate          # Linux/Mac: source venv/bin/activate
pip install -r requirements.txt
copy .env.example .env         # Linux/Mac: cp .env.example .env
```
1. Edita `.env` con tus datos de prueba.
2. Ejecuta `database.sql` en MySQL (crea la base `festival_votos` y el usuario).
3. Migraciones y datos:
```
python manage.py makemigrations votaciones
python manage.py migrate
python manage.py createsuperuser
python manage.py cargar_datos_prueba
python manage.py runserver
```
Sitio: http://127.0.0.1:8000/ — Admin: http://127.0.0.1:8000/admin/

## Rutas
`/` inicio · `/categorias/` · `/edicion/<id>/categorias/` · `/categoria/<id>/participantes/` · `/registro/` · `/login/` (documento + contraseña) · `/logout/` · `/admin/`

El diseño proviene del frontend React (Figma Make) portado a plantillas Django; los datos se leen de MySQL.
