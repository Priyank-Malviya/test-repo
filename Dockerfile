# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
COPY requirements.txt /home/app/
RUN pip install --no-cache-dir -r /home/app/requirements.txt

# copy files required for the app to run
COPY app.py /home/app/
COPY templates/* /home/app/templates/

# tell the port number the container should expose
EXPOSE 5000

# run the application
CMD ["python", "/home/app/app.py"]
