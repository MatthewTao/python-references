import datetime as dt
import json
import pika


def send_message(channel, message):
    channel.basic_publish(
        exchange="",
        routing_key="task_queue",
        body=message,
        properties=pika.BasicProperties(delivery_mode=pika.DeliveryMode.Persistent),
    )
    print(f" {dt.datetime.now().isoformat()} Sent {message}")


class ResultsReceiver:
    def __init__(self, channel, expected_results):
        self.channel = channel
        self.queue_name = "task_result"
        channel.queue_declare(queue=self.queue_name, durable=True)
        self.results = []
        self.expected_results = expected_results

    def _callback(self, ch, method, properties, body):
        decoded_message = json.loads(body.decode())
        self.results.append(decoded_message)

        print(f"{len(self.results)} results received")
        if len(self.results) == self.expected_results:
            raise StopIteration

    def wait_till_all_results_received(self):
        print(f" {dt.datetime.now().isoformat()} Start waiting for results")
        self.channel.basic_consume(
            queue=self.queue_name, on_message_callback=self._callback, auto_ack=True
        )
        try:
            self.channel.start_consuming()
        except StopIteration:
            print(f" {dt.datetime.now().isoformat()} All results received")
            print(f"{self.results}")


if __name__ == "__main__":
    with pika.BlockingConnection(
        pika.ConnectionParameters(host="localhost")
    ) as connection:
        channel = connection.channel()
        queue_name = "task_queue"
        channel.queue_declare(queue=queue_name, durable=True)
        print("Connection opened")

        # Send multiple messages
        for i in range(10):
            if i % 2 == 0:
                duration = 5
            else:
                duration = 10

            payload = json.dumps({"task_id": i, "task_duration": duration})
            send_message(channel, payload)

        print(f" {dt.datetime.now().isoformat()} All messages sent now")
        receiver = ResultsReceiver(channel, 10)
        receiver.wait_till_all_results_received()
