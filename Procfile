web: gunicorn mac.wsgi --log-file -
web: bin/start-nginx unicorn -c config/unicorn.rb gunicorn -c gunicorn.conf.py MyApp.wsgi
