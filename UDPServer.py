from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('',serverPort))
print 'waiting for message...'
while True:
	data, clientAddress = serverSocket.recvfrom(2048)
	print 'I received',data
	modifiedMessage = data.upper()
	serverSocket.sendto(modifiedMessage, clientAddress)
serverSocket.close()