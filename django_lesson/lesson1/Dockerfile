FROM python:3.7

RUN pip install django

COPY ./lesson1 /app/lesson1
COPY ./manage.py /app
COPY ./templates /app/templates

WORKDIR /app

EXPOSE 8000

CMD python manage.py runserver 0:8000
