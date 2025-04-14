# Use official Python image
FROM python:3.12-slim

# Create non-root user
RUN adduser --disabled-password --gecos "" user11

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY app.py .

# Change ownership
RUN chown -R user11:user11 /app

# Switch to non-root user
USER user11

# Expose Flask port
EXPOSE 5000

# Run app
CMD ["python", "app.py"]