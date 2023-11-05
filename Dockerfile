# Use the official Python image as the base image
FROM python:3.8-slim-buster

# Set the working directory
WORKDIR /usr/src/app

# Copy the requirements file into the container
COPY requirements.txt ./

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# CMD ["gunicorn", "patientData.wsgi:application", "--bind", "0.0.0.0:8000"]