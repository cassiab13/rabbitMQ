
import pika
import sys

from config import RABBITMQ_QUEUE
from connection import create_connection

def main(message):

    connection = create_connection()
    channel = connection.channel()

    channel.queue_declare(queue=RABBITMQ_QUEUE)
    channel.basic_publish(
        exchange='',
        routing_key=RABBITMQ_QUEUE, 
        body=message,
        properties=pika.BasicProperties(
            delivery_mode=pika.DeliveryMode.Persistent
        ))
    print(f"[x] Enviou: {message}")

    connection.close()

if __name__ == "__main__":
    message = ''.join(sys.argv[1:]) or "Hello World"
    main(message)
