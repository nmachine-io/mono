FROM python:3.6.1-alpine

WORKDIR /app

ADD selfie-hub/requirements.txt .
RUN pip3 install -r requirements.txt

ADD selfie-hub/. /app
RUN mkdir k8_kat && mkdir wiz && rm /app/.env
ADD k8_kat k8_kat
ADD wiz wiz

ENV LC_ALL=C.UTF-8 \
    LANG=C.UTF-8 \
    CONNECT_AUTH_TYPE=in \
    KAT_ENV=production \
    FLASK_ENV=production

EXPOSE 5000

CMD ["python3", "app.py"]