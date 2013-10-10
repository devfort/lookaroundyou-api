FROM ubuntu:12.04
MAINTAINER Ben Firshman "ben@firshman.co.uk"

RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list
RUN apt-get -qq update
RUN apt-get install -y git python-dev python-pip python-psycopg2 binutils libproj-dev gdal-bin
RUN useradd user

# Add code
ADD . /opt
WORKDIR /opt

# Install Python dependencies
RUN pip install -r requirements.txt
RUN DATABASE_URL="sqlite://:memory:" ./manage.py collectstatic --noinput

EXPOSE 8000
USER user
CMD ["gunicorn", "lookaroundyou_api.wsgi", "-b", "0.0.0.0:8000", "-k", "eventlet", "-w", "4"]

