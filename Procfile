release: bash postdeploy.sh && python manage.py migrate
web: gunicorn config.wsgi --log-file -
