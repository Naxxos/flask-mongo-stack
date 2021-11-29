FROM python:3.7-alpine

ARG no_proxy
ARG http_proxy
ARG https_proxy
ARG http_proxy_auth
ARG PYPI_URL
ARG PYPI_HOST

ENV GROUP_ID=1000 \
    USER_ID=1000

WORKDIR /var/www/

ADD . /var/www/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install gunicorn

RUN addgroup -g $GROUP_ID www
RUN adduser -D -u $USER_ID -G www www -s /bin/sh

USER www

EXPOSE 5000

CMD [ "gunicorn", "-w", "2", "--bind", "0.0.0.0:5000", "wsgi"]