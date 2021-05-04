![alt text](https://hackernoon.com/hn-images/1*cQmd2JsuqNwNelHh6bU-JA.jpeg)

# To build a Docker image

* Go to the desired folder location
* Run the following code to build an image:

		docker build -t <tag_of_the_image> .

# To run the built Docker image

* Go to the desired folder location
* Run the following code to build an image:

        docker run <tag_of_the_image>

# Deleting Docker containers

* Run the following command to see a list of your containers:

        docker ps

        # OR #

        docker ps -a # to see all containers, including those not running

**Note: Removing a Container is FINAL.**

## Deleting ***a single*** containter

1. Run **docker ps -a** and retrieve the <container_ID>. 
2. Run **docker rm <container_ID>** to remove ***just*** that container.

## Deleting ***all*** your containers:

To delete ***all*** your containers, run:

        docker ps -q -a | xargs docker rm

* **-q** prints only the container id
* **-a** prints all containers
* passing all container IDs to xargs, docker rm deletes all containers

# Deleting Docker images

## Delete a single image

1. Retrieve the Image ID using docker images (The <image_id> should be in the third column.)

2. Run docker rmi <image_id>

## Delete All Untagged Images

This requires a little bit of Linux magic (like deleting all containers above). Docker marks images without tags with "<none>" so we need to process only those images. Run the following command from your terminal (the awk programming language gives you text manipulation tools):

        docker rmi $(docker images | grep "<none>" | awk '{print $3}')

## Delete All Images

To delete ***all*** of your images, you can simplify the command above:

        docker rmi $(docker images | awk '{print $3}')
