# Python ka stable version use kar rahe hain
FROM python:3.10-slim-buster

# System dependencies install karna (speed ke liye)
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends gcc libffi-dev musl-dev ffmpeg python3-pip

# Working directory set kar rahe hain
WORKDIR /app

# Requirements copy karke install karna
COPY requirements.txt .
RUN pip3 install --no-cache-dir -U -r requirements.txt

# Baaki saari files copy karna
COPY . .

# Bot ko run karne ki command (Angel.py use kar rahe hain)
CMD ["python3", "Angel.py"]
