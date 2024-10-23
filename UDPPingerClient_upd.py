import socket
import time

# endereço servidor e porta
serverAddress = ("127.0.0.1", 12000)

# open socket UDP
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSocket.settimeout(2)  # timeout para receber respostas

num_pings = 10
rtt_list = []
lost_packets = 0

for i in range(1, num_pings + 1):
    message = f"PING {i}"
    start_time = time.time()
    
    try:
        # send mensagem para o servidor
        clientSocket.sendto(message.encode(), serverAddress)
        
        # receiv resposta do servidor
        response, server = clientSocket.recvfrom(1024)
        
        # calculo RTT
        rtt = (time.time() - start_time) * 1000  # conversão para milissegundos
        rtt_list.append(rtt)
        
        print(f"Recebido: {response.decode()} - RTT: {rtt:.2f} ms")
    except socket.timeout:
        print(f"PING {i} falhou (timeout)")
        lost_packets += 1

# close socket
clientSocket.close()

# calculo métricas
if rtt_list:
    rtt_min = min(rtt_list)
    rtt_max = max(rtt_list)
    rtt_avg = sum(rtt_list) / len(rtt_list)
    loss_rate = (lost_packets / num_pings) * 100

    print(f"\nMétricas após {num_pings} pings:")
    print(f"RTT Mínimo: {rtt_min:.2f} ms")
    print(f"RTT Máximo: {rtt_max:.2f} ms")
    print(f"RTT Médio: {rtt_avg:.2f} ms")
    print(f"Taxa de Perda de Pacotes: {loss_rate:.2f}%")
