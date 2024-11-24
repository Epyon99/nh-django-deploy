@echo off

REM Ejecutar collectstatic para recopilar archivos estáticos
echo Running collectstatic...
python manage.py collectstatic --noinput

REM Iniciar el servidor Django con Gunicorn
gunicorn --bind=0.0.0.0:8000 tiendasegura.wsgi:application
