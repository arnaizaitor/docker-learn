# To build the Docker image:

        docker build -t <pytest> .

# To run the docker image:

        docker run <pytest>

# To delete the Docker container:

        docker ps -a

        docker rm <container_id>

# To delete the docker image:

        docker images

        docker rmi <image_id>