# Dockerfile
FROM python:3.8-slim
WORKDIR /usr/src/app
COPY . .
CMD ["python", "./data_processor.py"]
