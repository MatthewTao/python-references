# RabbitMQ demo

Just make sure that RabbitMQ is running locally on a container or something, and that pika is installed

> pip install pika

Sample Docker compose file:
```
services:
  rabbitmq:
    image: rabbitmq:3-management
    container_name: 'rabbitmq'
    ports:
        - 5672:5672
        - 15672:15672
```
