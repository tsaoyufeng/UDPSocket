from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('',serverPort))
while True:
	print 'waiting for message...'
	data, clientAddress = serverSocket.recvfrom(2048)
	modifiedMessage = data.upper()
	serverSocket.sendto(modifiedMessage, clientAddress)
serverSocket.close()