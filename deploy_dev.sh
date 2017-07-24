#! /bin/zsh

python manage.py makemigrations && python manage.py migrate && python manage.py collectstatic --faster --use-multiprocessing --noinput

zappa undeploy dev -y

zappa deploy dev