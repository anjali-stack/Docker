# Docker
Docker
To execute the Dockerfile:

1. Unzip the .tar file from the compressed archive.
2. Load the Docker image using the command: `docker load -i filename.tar`
3. Start a container from the image with the command: `docker run -v local/dir:/home/data image_name`, where `local/dir` is the path to the directory on your host machine and `image_name` is the name of your Docker image.
