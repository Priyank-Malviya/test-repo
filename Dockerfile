# Use an official Python runtime as the base image
FROM python:3.9

EXPOSE 8002
# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code to the working directory
COPY . .

# Specify the command to run your application
CMD ["python", "app.py"]
