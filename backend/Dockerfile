FROM python:3.7-alpine as base
FROM base as builder

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1 #Prevents Python from writing pyc files to disc (equivalent to python -B option)
ENV PYTHONUNBUFFERED 1

WORKDIR /local

# install dependencies
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql \
    && apk add postgresql-dev \
    && apk add jpeg-dev zlib-dev libjpeg


COPY ./requirements.txt ./requirements.txt

#RUN pip install --install-option="--prefix=/local" -r ./requirements.txt
RUN pip install --user -r requirements.txt

FROM base

WORKDIR /src

#COPY --from=builder /local /usr/local/
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

RUN apk --no-cache add libpq

COPY ./src /src
COPY ./src/entrypoint.sh /src/entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
