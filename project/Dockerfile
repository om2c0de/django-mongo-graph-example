# Pull official image
FROM python:3

# Set work directory
WORKDIR /usr/src/app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy project to image (as root user for now)
COPY . .

# Install os dependencies
RUN apt update -y && apt install make automake gcc g++ subversion python3-dev libldap2-dev libsasl2-dev libssl-dev -y

# Install python dependencies
RUN pip install -r requirements.txt

# Run server
CMD python manage.py runserver 0.0.0.0:8000
