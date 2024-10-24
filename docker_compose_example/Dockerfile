# Use the official Python 3.12 slim image as the base image
FROM python:3.12-slim

# Set the working directory within the container
WORKDIR /flask

# First copy the requirements.txt, this won't change often
COPY requirements.txt .

# Upgrade pip and install Python dependencies
RUN pip3 install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Now copy the application
COPY app.py .

# Expose port 5000 for the Flask application
EXPOSE 5000

# Define the command to run the Flask application
CMD ["flask","--app", "app", "run", "--host=0.0.0.0"]