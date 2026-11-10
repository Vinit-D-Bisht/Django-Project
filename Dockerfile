
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy Django project
COPY . .

EXPOSE 8080

# Run Django using Gunicorn
CMD ["sh", "-c", "python manage.py migrate && gunicorn todo_project.wsgi:application --bind 0.0.0.0:8080"]
