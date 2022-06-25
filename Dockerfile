FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

RUN pip install pipenv

RUN apt-get update && apt-get install -y --no-install-recommends gcc

COPY . /code/

RUN pipenv install --system

CMD python manage.py runserver 0.0.0.0:$PORT