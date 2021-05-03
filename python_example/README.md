# Generic python project Dockerfile

        FROM python:3

        WORKDIR /usr/src/app

        COPY requirements.txt ./
        RUN pip install --no-cache-dir -r requirements.txt

        COPY . .

        CMD [ "python", "./your-daemon-or-script.py" ]

# To build the Docker image:

        docker build -t <image_tag> .

# To run the Docker image:

        docker run <image_tag>

# To delete the Docker container:

        docker ps -a

        docker rm <container_id>

# To delete the Docker image:

        docker images

        docker rmi <image_id>
