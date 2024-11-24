#!/bin/bash

# Activar el entorno virtual
source /home/site/wwwroot/venv/bin/activate

# Ejecutar migraciones
python manage.py migrate

# Recoger archivos estáticos
python manage.py collectstatic --noinput

# Iniciar Gunicorn
gunicorn --bind 0.0.0.0:8000 tiendasegura.wsgi:application
