# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY app/ ./app

# Expose port for Cloud Run / GKE
ENV PORT=8080
EXPOSE 8080

# Run the app
CMD ["python", "app/main.py"]
