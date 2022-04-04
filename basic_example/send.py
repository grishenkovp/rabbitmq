import pika

parameters = (pika.ConnectionParameters(host='localhost', 
                                        connection_attempts=5, 
                                        retry_delay=1))

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()