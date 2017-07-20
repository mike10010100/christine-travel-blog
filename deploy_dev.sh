#! /bin/zsh

python manage.py makemigrations && python manage.py migrate && python manage.py collectstatic --faster --noinput

zappa deploy dev