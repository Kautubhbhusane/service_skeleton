# light-weight python package
FROM python:3.11-slim            

# working directory inside container
WORKDIR /code

# requirements file
COPY requirements.txt .

# Python dependencies
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the entire app directory
COPY ./app /code/app

# Expose port 8000
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]