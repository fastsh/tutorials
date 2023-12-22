

# FROM python:3.11-alpine
FROM python:3.11-alpine as requirements-stage

WORKDIR /tmp

RUN apk update && apk upgrade --no-cache && \
    apk add --no-cache curl gcc libc-dev libffi-dev && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    apk del gcc libc-dev libffi-dev && \
    mv /root/.local/bin/poetry /usr/local/bin

COPY ./devops/pyproject.toml ./poetry.lock* /tmp/
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes


FROM python:3.11-alpine

WORKDIR /work

COPY ./app/api /work/api/
COPY --from=requirements-stage /tmp/requirements.txt /work/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /work/requirements.txt

EXPOSE 8000

CMD uvicorn --host 0.0.0.0 api.main:app --reload

