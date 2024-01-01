import pika

connection_paramters = pika.ConnectionParameters(
    host="localhost",
    port=5672,
    credentials=pika.PlainCredentials(
        username="guest",
        password="guest"
    )
)

# Conexão a fila
channel = pika.BlockingConnection(connection_paramters).channel()

channel.basic_publish(
    exchange="data_exchange",
    routing_key="",
    body="estouMandandoUmaMensagem",
    properties=pika.BasicProperties(
        delivery_mode=2
    )
)
