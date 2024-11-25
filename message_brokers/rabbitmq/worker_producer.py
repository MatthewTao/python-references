import datetime as dt
import pika


def send_message(connection, message):
    channel = connection.channel()

    channel.queue_declare(queue="task_queue", durable=True)

    channel.basic_publish(
        exchange="",
        routing_key="task_queue",
        body=message,
        properties=pika.BasicProperties(delivery_mode=pika.DeliveryMode.Persistent),
    )
    print(f" {dt.datetime.now().isoformat()} Sent {message}")


if __name__ == "__main__":
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    print("Connection opened")

    # Send multiple messages
    for i in range(5):
        if i % 2 == 0:
            send_message(connection, f"Task {i} ........")
        else:
            send_message(connection, f"Small Task {i} .")
    connection.close()

    print("Connection closed now")
    # Open up multiple worker_consumers and see how the messages get split up
