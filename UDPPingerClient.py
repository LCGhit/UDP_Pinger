import sys
import time
from socket import *

# Check command line arguments
if len(sys.argv) != 3:
    print('Usage: python UDPPingerClient <server ip address> <server port no>')
    sys.exit()

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
clientSocket = socket(AF_INET, SOCK_DGRAM)

# To set waiting time of one second for reponse from server
clientSocket.settimeout(1)

# Declare server's socket address
remoteAddr = (sys.argv[1], int(sys.argv[2]))

# list of round trip times
rtt_list = []
def calculateMin(myList):
    result = myList[0]
    for i in range(1, len(myList)):
        if myList[i] < result:
            result = myList[i]
    return result

def calculateMax(myList):
    result = myList[0]
    for i in range(1, len(myList)):
        if myList[i] > result:
            result = myList[i]
    return result

def calculateMean(myList):
    result = 0
    for i in myList:
        result += i
    return result/len(myList)


# Ping ten times
for i in range(10):
    sendTime = time.time()
    message = 'PING ' + str(i + 1) + ' ' + str(time.strftime('%H:%M:%S'))
    clientSocket.sendto(message.encode('utf-8'), remoteAddr)

    try:
        data, server = clientSocket.recvfrom(1024)
        recdTime = time.time()
        rtt = recdTime - sendTime
        rtt_list.append(rtt)
        print('Message Received', data.decode('utf-8'))
        print('Min Round Trip Time', calculateMin(rtt_list))
        print('Max Round Trip Time', calculateMax(rtt_list))
        print('Mean Round Trip Time', calculateMean(rtt_list))
        print('Round Trip Time', rtt)

    except timeout:
        print('REQUEST TIMED OUT')
        print
