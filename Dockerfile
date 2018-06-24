FROM alpine:latest

RUN apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache

RUN apk add --no-cache postgresql-dev gcc python3-dev musl-dev

WORKDIR /app
COPY ./ ./

RUN pip install -r requirements.txt

CMD ["gunicorn", "--config", "./gunicorn_config.py", "user.instance:app"]
