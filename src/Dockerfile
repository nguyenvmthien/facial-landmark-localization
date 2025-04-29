FROM us-docker.pkg.dev/deeplearning-platform-release/gcr.io/base-cu124.py310 AS base
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

RUN git clone https://github.com/Kartik-3004/facexformer.git
RUN pip install -r facexformer/requirements.txt


