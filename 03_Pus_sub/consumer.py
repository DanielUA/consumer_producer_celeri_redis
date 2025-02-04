import sys
import os
import json
import pika

def main():
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials)
    )
    channel = connection.channel()

    # Создаем обменный пункт, если он еще не существует
    channel.exchange_declare(exchange='Web16 event message', exchange_type='fanout')

    # Объявляем временную очередь
    q = channel.queue_declare(queue='', exclusive=True)
    name_q = q.method.queue

    # Привязываем очередь к обменному пункту
    channel.queue_bind(exchange='Web16 event message', queue=name_q)

    def callback(ch, method, properties, body):
        message = json.loads(body.decode())
        print(f" [x] Received {message}")

    channel.basic_consume(queue=name_q, on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
