#!/bin/bash

# Navegar para o diretório do projeto Django, se necessário
# cd /path/to/your/django/project

# Realizar migrações
python manage.py makemigrations


python manage.py migrate

# Iniciar o servidor
python manage.py runserver 0.0.0.0:8000
