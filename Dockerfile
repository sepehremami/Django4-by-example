FROM python:3-alpine

WORKDIR /usr/src/app

COPY requirements.txt .

RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 python -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]