# Use lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Prevent Python buffering
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Upgrade pip (VERY IMPORTANT for dependency resolution)
RUN pip install --upgrade pip

# Copy requirements first (for cache optimization)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port (Streamlit: 8501 | FastAPI: 8000)
EXPOSE 8501

# Start app (Streamlit example)
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]