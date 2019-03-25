FROM python:3.7
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV UWSGI_WSGI_FILE=/src/chrity_backend/wsgi.py
ENV UWSGI_HTTP=0.0.0.0:8080
ENV UWSGI_MASTER=1
ENV UWSGI_WORKERS=2
ENV UWSGI_THREADS=8
ENV UWSGI_UID=1000
ENV UWSGI_GID=2000
ENV UWSGI_LAZY_APPS=1
ENV UWSGI_WSGI_ENV_BEHAVIOR=holy
RUN mkdir /src
WORKDIR /src
ADD ./src /src
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8080

CMD ["uwsgi", "--http-auto-chunked", "--http-keepalive"]
