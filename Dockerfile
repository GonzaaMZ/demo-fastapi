# Utiliza la imagen oficial de Python 3.11.4 como base
# FROM python:3.11.4

# WORKDIR /code

# # 
# COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt

# COPY . .

# # 
# # CMD ["uvicorn", "app.main:app", "--host", "127.0.0.1", "--port", "8000"]

FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
COPY requirements.txt /
RUN pip install -r /requirements.txt
COPY ./app /app/app