FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY Pipfile* /app/

RUN pip install pipenv && pipenv install --system --deploy --ignore-pipfile
COPY . .

COPY entrypoint.sh /app/
RUN chmod +x entrypoint.sh

COPY . /app/

CMD ./entrypoint.sh