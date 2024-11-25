import datetime as dt
import pika
import sys
import os


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    channel = connection.channel()

    channel.exchange_declare(exchange="logs", exchange_type="fanout")

    queue_declare_result = channel.queue_declare(queue="", exclusive=True)
    # Where queue name is blank, a random temporary queue would be chosen.
    # But that is fine with the fanout exchange as the queue doesn't matter too much

    queue_name = queue_declare_result.method.queue

    channel.queue_bind(exchange="logs", queue=queue_name)

    def callback(ch, method, properties, body):
        print(f" {dt.datetime.now().isoformat()} {body}")

    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

    print(f" {dt.datetime.now().isoformat()} Waiting for logs. To exit press CTRL+C")
    channel.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
