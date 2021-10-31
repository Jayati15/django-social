web: gunicorn social_clone.wsgi
release: python manage.py makemigrations --noinput
release: python manage.py collecstatic --noinput
release: python manage.py migrate --noinput