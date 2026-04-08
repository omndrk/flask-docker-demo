FROM python:3.14-alpine

WORKDIR /app

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN adduser -D appuser
USER appuser

EXPOSE 8000

CMD ["python", "app.py"]