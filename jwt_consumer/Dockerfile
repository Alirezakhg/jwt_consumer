# jwt_consumer Dockerfile
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . /app/

# Expose port 8001
EXPOSE 8001

# Run the application
CMD ["gunicorn", "jwt_consumer.wsgi:application", "--bind", "0.0.0.0:8001"]
