FROM python:3.10

WORKDIR /app

COPY requirements/app.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 80

CMD ["uvicorn", "app.main:app", "--log-level", "debug", "--host", "0.0.0.0", "--port", "80", "--root-path", "/api_template"]