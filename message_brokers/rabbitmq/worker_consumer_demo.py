import datetime as dt
import json
import time
import pika, sys, os


class Worker:
    def __init__(self, channel):
        self.channel = channel
        channel.queue_declare(queue="task_queue", durable=True)
        channel.queue_declare(queue="task_result", durable=True)

    def run(self):
        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(
            queue="task_queue", on_message_callback=self._callback, auto_ack=False
        )

        print(
            f" {dt.datetime.now().isoformat()} Waiting for messages. To exit press CTRL+C"
        )
        self.channel.start_consuming()

    def _callback(self, ch, method, properties, body: bytes):
        decoded_message = json.loads(body.decode())

        print(f" {dt.datetime.now().isoformat()} Received {decoded_message}")

        # Count the number of . in the message and use sleep to simulate processing
        time.sleep(decoded_message.get("task_duration"))

        print(
            f" {dt.datetime.now().isoformat()} Task {decoded_message.get('task_id')} is now processed"
        )

        # Reply and acknowledge that message is successfully processed and can be deleted
        ch.basic_ack(delivery_tag=method.delivery_tag)

        # Send message with results
        self._send_result(
            ch,
            json.dumps(
                {"task_id": decoded_message.get("task_id"), "status": "success"}
            ),
        )

    def _send_result(self, channel, message):
        channel.basic_publish(
            exchange="",
            routing_key="task_result",
            body=message,
            properties=pika.BasicProperties(delivery_mode=pika.DeliveryMode.Persistent),
        )
        print(f" {dt.datetime.now().isoformat()} Sent {message}")


def main():
    with pika.BlockingConnection(
        pika.ConnectionParameters(host="localhost")
    ) as connection:
        channel = connection.channel()

        worker = Worker(channel)
        worker.run()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
