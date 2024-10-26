import pika
from config import RABBITMQ_HOST, RABBITMQ_PORT

def create_connection():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=RABBITMQ_HOST, port=RABBITMQ_PORT)
    )
    return connection
