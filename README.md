![docker](https://user-images.githubusercontent.com/38442315/117026161-d7124680-acfb-11eb-8bdb-f2aadd412052.jpg)

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

1. Run ```docker ps -a``` and retrieve the <container_ID>. 
2. Run ```docker rm <container_ID>``` to remove ***just*** that container.

## Deleting ***all*** your containers:

To delete ***all*** your containers, run:

        docker ps -q -a | xargs docker rm

* ```-q``` prints only the container id
* ```-a``` prints all containers
* passing all container IDs to xargs, docker rm deletes all containers

# Deleting Docker images

## Delete a single image

1. Retrieve the Image ID using ```docker images``` (The <image_id> should be in the third column.)

2. Run ```docker rmi <image_id>```

## Delete All Untagged Images

This requires a little bit of Linux magic (like deleting all containers above). Docker marks images without tags with "<none>" so we need to process only those images. Run the following command from your terminal (the awk programming language gives you text manipulation tools):

        docker rmi $(docker images | grep "<none>" | awk '{print $3}')

## Delete All Images

To delete ***all*** of your images, you can simplify the command above:

        docker rmi $(docker images | awk '{print $3}')
	
	
# [Docker images vs Docker containers](https://www.whitesourcesoftware.com/free-developer-tools/blog/docker-images-vs-docker-containers/)

![container](https://user-images.githubusercontent.com/38442315/117031311-bb5d6f00-ad00-11eb-8b4b-a30dce0ac7f0.jpg)

## What is a Docker Image?

A Docker image is a read-only, inert template that comes with instructions for deploying containers. In Docker, everything basically revolves around images.

An image consists of a collection of files (or layers) that pack together all the necessities—such as dependencies, source code, and libraries—needed to set up a completely functional container environment.

A Docker image is made up of multiple layers. The image layers are stacked to one another. Although the layers may be different from each other, every one of them may depend on the one immediately below it. 

These layers, also called intermediate images, are essentially read-only files that a container layer will be added on top of them after setting up a virtualized environment. 

You can use the ```docker images``` command to view an image’s details on your system.

Furthermore, you can also use the ```docker history <image_tag>``` command to see all the layers that make up the downloaded image.

## What is a Docker Container?

A Docker container is a virtualized runtime environment that provides isolation capabilities for separating the execution of applications from the underpinning system. It’s an instance of a Docker image.

Containers are the ultimate utility of the Docker technology—they provide a portable and lightweight environment for deploying applications.

Each container is autonomous and runs in its own isolated environment, ensuring it does not disrupt other running applications or its underlying system. This greatly improves the security of applications.

Docker defines several container states, such as created, restarting, running, paused, exited, and dead. Since several states are possible, and a container is just an instance of the image, a container does not need to be running.

Then, to view its details on your system, you can use either the ```docker ps``` command (outputs only running containers) or ```docker ps -a``` command (outputs both running and stopped containers). 

Every time Docker creates a container from an image, it places a thin read-write layer on top of the image. This writable layer allows for changes to be made to the container, as the lower layers in the image are unchangeable. It also stores any changes made to the container during its entire runtime.

If you want to keep the changes made to the initial image for future use, you can take a screenshot to save the current state of the container. This will add a container layer atop the image, eventually creating a new immutable image. 

Furthermore, it’s possible to launch multiple container instances simultaneously from the same image. Every container layer will maintain its own individual state safely atop the underlying image. The containers will have different IDs, but arise from the same image.

Creating multiple containers from the same image can be very beneficial. For example, it increases the availability of an application—in case one container fails, the others will ensure the application is still up and running. Duplicate containers also help in scaling up an application in case demand surges upwards.

## What is the difference between Docker Images and Docker Containers?

Docker images and containers work together to let you unleash the full potential of the innovative Docker technology. However, they have subtle differences that may be difficult to notice, especially for a beginner.

A simple analogy that compares their differences is to think of a Docker image as a recipe and a container as the cake prepared from that recipe.

The recipe sets out the instructions for baking the cake. You cannot enjoy eating the cake if you do not put the instructions into action. 

You need to follow the recipe to prepare the cake and eat it. Similarly, you should follow the instructions in the Docker image to create and start a container, and enjoy the benefits of Docker.

You can bake as many cakes as possible from a single recipe—just like an image can create multiple containers. However, if you change the recipe, the taste of your existing cakes will not change. 

Only newly baked cakes will use the modified recipe. Likewise, if you make changes to a container image, you’ll not affect the already running containers.

Here is a table that points out the differences between Docker images and containers:

|                      *****```Docker Image```*****                     |                             *****```Docker Container```*****                            |
|:----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| It's a container blueprint                                 | It's an image instance                                                      |
| It's immutable                                             | It's writable                                                               |
| It can exist without a container                           | A container must run an image to exist                                      |
| Does not need computing resources to operate               | Needs computing resources to run -containers run as Docker virtual machines |
| It can be shared via a public or private registry platform | No need to share an already running entity                                  |
| Created only once                                          | Multiple containers can be created from the same image                      |
