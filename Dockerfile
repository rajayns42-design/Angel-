FROM python:3.10-slim-buster

# Fix for expired Debian repositories
RUN sed -i 's/deb.debian.org/archive.debian.org/g' /etc/apt/sources.list && \
    sed -i 's|security.debian.org/debian-security|archive.debian.org/debian-security|g' /etc/apt/sources.list && \
    sed -i '/stretch-updates/d' /etc/apt/sources.list

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    gcc \
    libffi-dev \
    musl-dev \
    ffmpeg \
    python3-pip

COPY . /app
WORKDIR /app
RUN pip3 install --no-cache-dir -U -r requirements.txt

CMD ["python3", "Angel.py"]
