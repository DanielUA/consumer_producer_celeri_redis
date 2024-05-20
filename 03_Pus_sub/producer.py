from datetime import datetime
import json
import pika

# Настройка соединения с RabbitMQ
credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

# Объявляем обменный пункт 'Web16 event message', если он еще не существует
channel.exchange_declare(exchange='Web16 event message', exchange_type='fanout')

# Функция для создания и отправки события
def create_event():
    message = {
        'event': 'Test event',
        'message': 'Test message',
        'detail': f'Date: {datetime.now().isoformat()}'
    }
    # Публикуем сообщение в обменный пункт
    channel.basic_publish(exchange='Web16 event message', routing_key='', body=json.dumps(message).encode())
    print(" [x] Sent 'Test event'")
    connection.close()

if __name__ == "__main__":
    create_event()
