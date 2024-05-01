FROM python:3.10-slim
LABEL authors="Ennis M. Salam"

WORKDIR /app

COPY ./api/* /app/

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

ENV POSTGRES_DB=postgres
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=postgres

CMD ["python", "app.py"]
