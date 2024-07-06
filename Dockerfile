FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.tx

COPY . .

# Expose the port that the app will run on
EXPOSE 5050

# Define the command to run the application
CMD ["python", "app.py"]
