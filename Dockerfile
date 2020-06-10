# FROM python:3.6.1-alpine
# FROM surnet/alpine-python-wkhtmltopdf:3.7.2-0.12.5-small
FROM surnet/alpine-python-wkhtmltopdf:3.7.2-0.12.5-full
WORKDIR /app
ADD . /app

RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps
 
EXPOSE 4000

CMD ["python3", "run.py"]
