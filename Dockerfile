FROM python:3.7

# Install sqlite3
RUN apt-get update && apt-get install -y sqlite3

# Install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Copy source code
COPY . /app

# Set working directory
WORKDIR /app

CMD ["python", "init_db.py"]

CMD ["python", "app.py"]