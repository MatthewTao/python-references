import datetime as dt
import pika
import sys


if __name__ == "__main__":
    message = " ".join(sys.argv[1:]) or "Hello World!"
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    channel = connection.channel()

    channel.queue_declare(queue="hello")

    channel.basic_publish(exchange="", routing_key="hello", body=message)
    print(f" {dt.datetime.now().isoformat()} Sent {message}")
    connection.close()
