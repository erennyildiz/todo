FROM python:3.6

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /todo
# Set the working directory to /todo
WORKDIR /todo
ADD . /todo/
RUN pip install -r requirements.txt