web: python manage.py collectstatic -no-input
web: gunicorn mysite.wsgi
release: python manage.py migrate
