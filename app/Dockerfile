FROM python:3

#RUN pip freeze > requirements.txt

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 8080
CMD [ "gunicorn", "--bind", "0.0.0.0:8080","wsgi:app" ]
