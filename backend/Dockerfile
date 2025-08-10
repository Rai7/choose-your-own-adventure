FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port (will be overridden by Render's PORT env var)
EXPOSE 10000

# Use gunicorn with our configuration
CMD ["gunicorn", "-c", "gunicorn.conf.py", "main:app"]