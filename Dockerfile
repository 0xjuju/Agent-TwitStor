# Use an official Python runtime as a parent image
FROM python:3.11.6

# Set the working directory in the container
WORKDIR /home/autogen/autogen/myapp

# Copy the current directory contents into the container at /app
COPY . /home/autogen/autogen/myapp

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV NAME World

# Run python manage.py test when the container launches
CMD ["python", "manage.py", "test"]