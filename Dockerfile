# Use an official Python runtime as a base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

# Copy the entire src directory and the data directory into the container
COPY src ./src
COPY ./data ./data

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Update the working directory in the container
WORKDIR /app/src

# Set environment variables
ENV FLASK_APP=main.py
ENV FLASK_ENV=production

# Run the Flask application
#CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]
CMD gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
