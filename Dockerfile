FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files
COPY . .

# Expose port 8080
EXPOSE 8080

# Start the application using Streamlit
CMD ["streamlit", "run", "App.py", "--server.port", "8080", "--server.address", "0.0.0.0"]