ARG PYTHON_VERSION=3.11-slim-bullseye

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /code

WORKDIR /code

COPY requirements.txt /tmp/requirements.txt
RUN set -ex && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /root/.cache/
COPY she_codes_news/ /code/

ENV SECRET_KEY "jj3GWI3O0vK2tjsq8a1fymkPwjUmCEX8LU0kRGqad0TViqXTtt"
RUN chmod +x /code/run.sh

EXPOSE 8000

CMD ["/code/run.sh"]

