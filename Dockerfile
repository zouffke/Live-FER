FROM python:3.12-slim

WORKDIR /app

# Install necessary packages
RUN apt-get update && apt-get install -y libgl1 libglib2.0-0

COPY scripts .

RUN pip install --no-cache -r requirements.txt

EXPOSE 5000

CMD ["uvicorn", "app:asgi_app", "--host", "0.0.0.0", "--port", "5000"]