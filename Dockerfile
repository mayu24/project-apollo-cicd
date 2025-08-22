# Use slim Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Cloud Run expects app to listen on PORT env variable
ENV PORT=8080

# Expose port for container
EXPOSE 8080

# Run FastAPI with uvicorn
CMD ["python", "main.py"]
