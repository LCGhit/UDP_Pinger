import random
import sys
import time
from socket import *

# Check command line arguments
if len(sys.argv) != 2:
    print('Usage: python UDPPingerServer <server port no>')
    sys.exit()

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('', int(sys.argv[1])))

packages_num = 0
lost_packages = 0
lost_packages_percentage = 0
while True:
    packages_num += 1
    # Generate random number in the range of 0 to 10
    rand_1 = random.randint(0, 10)
    rand_2 = random.randint(0, 10)
    # Receive the client packet along with the address it is coming from

    message, address = serverSocket.recvfrom(1024)
    if (int(message.split()[1]) != rand_1):
        if (int(message.split()[1]) == rand_2):
            print('Delayed message: ', rand_2)
            time.sleep(3)
        message = message.decode('utf-8')  # convert bytes to string
        # Capitalize the message from the client
        message = message.upper()
        # the server responds
        serverSocket.sendto(message.encode('utf-8'), address)
    else:
        lost_packages += 1
        print('Ignored message: ', rand_1)
    print(f'Lost packages percentage: {(lost_packages/packages_num)*100}%')
