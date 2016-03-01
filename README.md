# celery

Container with [celery](http://www.celeryproject.org/) based on ubuntu

The container is configured to use a celery configuration file and a sample app that must be replaced by your app (change in config file your app details and mount it with -v).

To start the container execute the following commands (docker >= 1.9):

docker run --name some-celery -v /var/docker_conf/celery:/etc/celery -v /var/docker_data/celery:/var/celery/db -d njordr/celery

You can find an example config in my [git repo](https://github.com/njordr/celery)
