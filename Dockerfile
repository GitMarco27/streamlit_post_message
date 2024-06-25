FROM python:3.10-slim

# Install Nginx
RUN apt-get update && apt-get install -y nginx

# Install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy application code
COPY . /app
WORKDIR /app

# Copy Nginx configuration
COPY nginx.conf /etc/nginx/sites-available/default

# Expose the port
EXPOSE 80

# Start services
CMD service nginx start && nohup streamlit run demo.py --server.port 8080 \
 --server.enableCORS false --server.enableXsrfProtection false \
 --server.headless=true & python -m http.server 8000
