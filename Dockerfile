# #FROM ubuntu:20.04
# #FROM python:3.9
# FROM alpine

# RUN apk add --no-cache python3

# #RUN apt-get update && apt-get install -y python3.9 python3.9-dev
# ADD /Limerick.txt /home/data/Limerick.txt
# ADD /IF.txt /home/data/IF.txt
# ADD /app.py /home/app.py
#  RUN mkdir -p /home/output/
# CMD ["/home/app.py"]
# ENTRYPOINT ["python3"]

FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /home
RUN mkdir -p /home/data /home/output

# Copy the Python script into the container
COPY . /home/data
# Copy result.txt to /home/output
RUN touch /home/output/result.txt

# Give execute permissions to script
RUN chmod +x /home/data/app.py
RUN chmod +w /home/output/result.txt

# Create the required directories


# Set the command to run the script
CMD ["python3", "/home/data/app.py"]
