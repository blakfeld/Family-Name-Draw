FROM ubuntu

# create user
# RUN groupadd www-data
RUN useradd -d /home/bottle -m bottle

# Update Sources
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list && apt-get update

# Install pip
RUN apt-get install python-pip -y

# Copy over the app
ADD family_gift_app/ /opt/family_gift_app/
RUN pip install bottle cherrypy

# Expose Port
EXPOSE 9001


ENTRYPOINT ["/usr/bin/python", "/opt/family_gift_app/app.py"]
USER bottle
