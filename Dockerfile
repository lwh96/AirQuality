FROM python:3

ARG SECRET_KEY
ENV SECRET_KEY $SECRET_KEY

RUN mkdir /code
WORKDIR /code
COPY . /code/
RUN pip install gunicorn django djangorestframework pandas

CMD gunicorn -w 3 airquality.wsgi --bind 0.0.0.0:8000
