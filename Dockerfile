# Use an official Python runtime as a parent image
FROM python:3.9.12-slim

# Update package index
# RUN apt-get update && apt-get install -y libgomp1

# Set the working directory to /app
WORKDIR /app

# Copy the files and directories into the container at /app
# COPY my_model.pth /app/my_model.pth
COPY . .


# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Install additional dependencies for the Colab notebook
# RUN pip install --no-cache-dir torch torchvision
RUN pip install torch==2.1.1+cpu torchvision==0.16.1+cpu -f https://download.pytorch.org/whl/torch_stable.html


# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run the Flask application
CMD ["python", "final_app.py"]
