FROM python:3.8-alpine

FROM jjanzic/docker-python3-opencv:latest

WORKDIR /app


# Install system dependencies and clean up


# Copy the requirements file first to leverage caching
COPY requirements.txt .

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Set environment variable for Tesseract


# Copy trained data for Tesseract

# Expose port
EXPOSE 8043

# Command to run the application
CMD ["python3", "app.py"]

RUN pip3 list