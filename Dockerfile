# Install airflow
FROM apache/airflow:2.9.0-python3.9 AS airflow
COPY ./requirements.txt requirements.txt

# Update system and install specific librairies for interact with geometrics layers
USER root
RUN apt-get clean \
    && apt-get autoclean \
    && apt-get update --fix-missing \
    && apt-get install -y \
    chromium \
    build-essential \
    python3-all-dev \
    libpq-dev \
    libgeos-dev \
    wget \
    curl \
    sqlite3 \
    cmake \
    unzip \
    git \
    libtiff-dev \
    libsqlite3-dev \
    libcurl4-openssl-dev \
    pkg-config \
    binutils \
    libproj-dev \
    gdal-bin \
    libgdal-dev g++ --no-install-recommends \
    && rm -r /var/lib/apt/lists/*

# Install librairies
USER airflow
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

ENV CHROME_EXECUTABLE_PATH=/usr/bin/chromium
ENV GIT_PYTHON_GIT_EXECUTABLE=/usr/bin/git

# Install sphinx
FROM sphinxdoc/sphinx AS sphinx
WORKDIR /docs

COPY ./requirements.txt /docs/requirements.txt
RUN pip install --no-cache-dir sphinx-autobuild furo