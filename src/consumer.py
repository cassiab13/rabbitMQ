import time
from connection import create_connection
from config import RABBITMQ_QUEUE

def callback(ch, method, properties, body):
    print(f"Received message: {body.decode()}")
    time.sleep(body.count(b'.'))
    ch.basic_ack(delivery_tag = method.delivery_tag)

def main():
    connection = create_connection()
    channel = connection.channel()
    
    channel.queue_declare(queue=RABBITMQ_QUEUE)
    
    channel.basic_consume(queue=RABBITMQ_QUEUE, on_message_callback=callback)
    
    channel.start_consuming()
    
if __name__ == "__main__":
    main()