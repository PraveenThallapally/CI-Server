FROM python:3.9-slim AS builder
 
# Set working directory
WORKDIR /app
 
# Install build dependencies
RUN apt-get update && apt-get install -y build-essential
 
# Copy requirements first (for caching)
COPY requirements.txt .
 
# Install dependencies into a temporary folder
RUN pip install --prefix=/install -r requirements.txt
 
 
# ---------- Stage 2: Runtime ----------
FROM python:3.9-slim
 
# Set working directory
WORKDIR /app
 
# Copy installed dependencies from builder
COPY --from=builder /install /usr/local
 
# Copy application code
COPY app.py .
 
# Expose port
EXPOSE 5000
 
# Run Flask app
CMD ["python3", "app.py"]

