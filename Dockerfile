FROM python:3

# Environment
WORKDIR /usr/src
COPY . /usr/src

# Container
EXPOSE 8200
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
