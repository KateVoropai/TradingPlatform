FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY Pipfile* /app/

RUN pip install pipenv && pipenv install --system --deploy --ignore-pipfile
COPY . .

ENTRYPOINT ["python", "trading_platform/manage.py"]
CMD ["runserver", "0.0.0.0:8000"]