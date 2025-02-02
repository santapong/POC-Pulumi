# Use an official Python base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy application files
COPY . /app

# Install system dependencies (for Ollama and Python dependencies)
RUN apt-get update && apt-get install -y \
    build-essential \
    libatlas-base-dev \
    python3-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# # Install Ollama (CLI)
# RUN curl -fsSL https://ollama.com/install.sh | sh

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# # Install Ollama's Python client & Langchain
# RUN pip install ollama langchain

# Ensure Ollama service is running before FastAPI starts
CMD uvicorn main:app --host 0.0.0.0 --port 8000
