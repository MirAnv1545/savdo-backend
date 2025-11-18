# Base image
FROM python:3.12-slim

# Workdir
WORKDIR /app

# Dependencies
COPY backend/requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project
COPY backend/ .

# Collect static files (agar kerak bo‘lsa)
RUN python manage.py collectstatic --noinput

# Port
EXPOSE 8000

# Run server
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
