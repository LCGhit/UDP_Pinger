import random
import time
import socket

# socket UDP
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# endereço IP e porta ao socket
serverSocket.bind(("127.0.0.1", 12000))

print("Servidor UDP pronto para receber...")

while True:
    # gerar número aleatório entre 0 e 10
    rand = random.randint(0, 10)
    
    # receiv do cliente o pacote junto com o endereço de onde veio o pacote
    message, address = serverSocket.recvfrom(1024)
    
    # converter a mensagem para maiúsculas
    message = message.upper()

    # 1. perda aleatória de pacotes: ignora a mensagem com uma chance de 30%
    if rand < 3:
        print("Pacote perdido")
        continue
    
    # 2. atraso aleatório de até 1 segundo
    delay = random.uniform(0, 1)
    time.sleep(delay)
    
    # send mensagem de volta para o cliente
    serverSocket.sendto(message, address)
    print(f"Mensagem enviada de volta após {delay:.2f}s de atraso")
