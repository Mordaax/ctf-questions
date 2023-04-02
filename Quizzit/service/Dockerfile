FROM python:latest
# Put files at the image '/server/' folder.
ADD socket-server.py /server/
# '/server/' is base directory
WORKDIR /server/
# Expose port 9898 in the container
EXPOSE 6105
# execute the command
CMD [ "python3", "/server/socket-server.py" ]