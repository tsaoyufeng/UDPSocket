from socket import *
serverName = '192.168.182.128'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
while True:
	message = raw_input('>')
	clientSocket.sendto(message,(serverName,serverPort))
	modifiedMessage,serverAddress = clientSocket.recvfrom(2048)
	print modifiedMessage
clientSocket.close()
