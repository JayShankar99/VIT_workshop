> Steps to dockerize

> Create `Dockerfile`

```bash
FROM python:latest

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install -r requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

> Upload the required files to `github` which includes `[Dockerfile, requirements.txt, streamlit file]`

> Create an `EC2` instance, {we have used ubuntu for this demo purpose}

> Execute the below commands once your instance is ready.

```bash
sudo apt-get update -y

sudo apt-get upgrade

#Install Docker

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

# Create group that can use docker

sudo usermod -aG docker ubuntu

newgrp docker

```

> Clone your repo from `github`

```bash
git clone "your-project"
```

> Build `Docker image`

```bash
docker build -t myapp . 
```

> Check if image has been build or not

```bash
docker images -a  
```

> Test if the image is running or not

```bash
docker run -d -p 8501:8501 myapp
```

> Check if any image/container is running or not

```bash
docker ps  
```

> Stop a running container

```bash
docker stop CONTAINER ID
```

> Delete any resedual of container that might consume memory.

```bash
docker rm $(docker ps -a -q)
```


