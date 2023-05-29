# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container

RUN pip install --no-cache-dir -r requirements.txt

# copy files required for the app to run

# tell the port number the container should expose
EXPOSE 5000

# run the application
CMD ["python", "app.py"]
