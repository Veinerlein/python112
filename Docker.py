DOCKER = "Сервіс для запуску додатків у контейнерах"
CYBERNETICS = "Надстройка для керування запуску різних контейнерів докер на різних серв5ерах"
# Applications started isolated from out environment
# Independed
# easy to start the conteiner in different computers
# All DEpendence iare installing inside the conteiner
# Easy to masshtabe in a way to ingrease amount of conteainer
# Good to use in devoloping

Conteiner = "The smollest element in the docker world (Many different containers - good for you)"
# Client =>   Daemon => HOST
# from 1 Image(Образ) I can create many different containers

# Repository - different versions of images (образів)
# Registry(Реєстр) - different versions of Repositories (Local or Farther(DOCKERHUB))

# linux - containers are reated by here
Linux_Kernel = "Ядро опер системи"  # REM , CPU, NETWORK, DISK, __DOCKER ENGINE__

DOCKER_ENGINE = "STARTED DOCKER DAEMON (Service)"

Container_1 = ["FIles"]  # Files are accepted only for this container .Process() - запуститься процес
DISK = [Container_1]

Container_2 = ['FILES2']# .process()
Container_3 = ['FILES3']# .Process() .Process2() - can contain few diff processes (more seldom)
# Files are Independent
# All containers on docker host uses all the same resources and it is need to control what container use that resource
# The processes are independent
# delete container = delete files
# if pricess is finished , docker will stop the container
# ON windows and Mac Os - to use Docker run a virtual machine
# Docker Desctop prigramm - virtual machine (Linux VM)
image = ["Container", "Container","Container"]
image = {
    "layer":"files",
    "layer2":"files",
    "layer3":"files",
    "Basic layer":"files"
         }
#Basic layer - saved 1 time only, ci=onstructed with any others layers

# Basic from Node.js is reusing from onoather image
# all layers are read only
# images can be removed and deleted
# images lives in repositories
# Official images (DockerHUB)
# Free images and private images
# Files => Layers => Image

# Repository Docker = different versions (Latest, 8.0.1 - tegs) latest - the actual version of image (образу)
#Docker Desctop for Windows
# Docker engine for Linux
#I WROTE IN VISUAL STUDIO CODE

#client and docker server are not depended

# Commands:
# docker version - To show the version
# docker ps -a  - list of started containers and containers who stopped
# docker images - local images
# docker run helloworld - creating container from imsge with name helloworld (Докер пошукаю на машині а  потім в неті образ з таким іменем, якщо знайде, то скачає та запустить контейнер на основі даного  образу)











