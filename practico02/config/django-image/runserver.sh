#!/bin/bash
set -e

if [ ! -f manage.py ]
then
    django-admin startproject app .
fi

sleep 10

python manage.py makemigrations
python manage.py migrate --noinput

if [[ ! -z "${DJANGO_SU_NAME}" ]]
then
    python manage.py shell -c "
from django.contrib.auth import get_user_model

User = get_user_model()

if not User.objects.filter(username='${DJANGO_SU_NAME}').exists():
    User.objects.create_superuser(
        '${DJANGO_SU_NAME}',
        '${DJANGO_SU_EMAIL}',
        '${DJANGO_SU_PASSWD}'
    )
"
fi

python manage.py runserver 0.0.0.0:8000
