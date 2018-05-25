import socket

# destination hostname
serverName = input('Specify the destination you want to connect:')
# destination port
serverPort = 12000
# create a client socket (UDP)
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    message = input('Input lowercase sentence:')
    clientSocket.sendto(str.encode(message), (serverName, serverPort))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print(bytes.decode(modifiedMessage))
clientSocket.close()
