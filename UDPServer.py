import socket

serverPort = 12000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print('Waiting for message...')
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = bytes.decode(message).upper()
    serverSocket.sendto(str.encode(modifiedMessage), clientAddress)
serverSocket.close()
