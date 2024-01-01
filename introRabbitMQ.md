O RabbitMQ utiliza o protocolo AMQP(Advanced Message Queuing Protocol)

Elementos AMQP
- Endereço IP e porta
- Producer / Consumer
- Mensagens gerenciadas em filas (Queues)
- Assincronismo


Existem dois agentes principais 

Producer
Aquele que faz a publicação da mensagem

a mensagem é redirecionada para uma fila(queue), essa fila é organizada em forma de pilha, e o consumer consome a fila.

Consumer
Aquele que consome a mensagem do producer

Exchanges
Ponto de entrada das mensagems

Tipos ---->


Queue

De forma assincrona, o consumer poder consumir a fila, e o producer pode fazer outra coisa.

---
RabbitMQ é um Broker AMQP
Espécie de Gerenciador do Protocolo