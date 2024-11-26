FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . ./api_server

EXPOSE 8080

CMD ["uvicorn", "api_server.main:app", "--host", "0.0.0.0", "--port", "8080"]
