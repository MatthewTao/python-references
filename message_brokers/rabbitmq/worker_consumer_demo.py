import datetime as dt
import time
import pika, sys, os


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    channel = connection.channel()

    channel.queue_declare(queue="task_queue", durable=True)

    def callback(ch, method, properties, body: bytes):
        decoded_message = body.decode()
        print(f" {dt.datetime.now().isoformat()} Received {decoded_message}")

        # Count the number of . in the message and use sleep to simulate processing
        time.sleep(decoded_message.count(".") * 2)

        print(f" {dt.datetime.now().isoformat()} {decoded_message} is now processed")

        # Reply and acknowledge that message is successfully processed and can be deleted
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(
        queue="task_queue", on_message_callback=callback, auto_ack=False
    )

    print(
        f" {dt.datetime.now().isoformat()} Waiting for messages. To exit press CTRL+C"
    )
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
