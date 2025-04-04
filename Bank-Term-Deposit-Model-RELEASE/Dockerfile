# Use an official Python runtime as a parent image
FROM python:3.9

# Copy the current directory contents into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Define the command to run the application
CMD ["python", "app.py"]
