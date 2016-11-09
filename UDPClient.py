from socket import *

#hostname
serverName = '192.168.182.128'
#port number
serverPort = 12000
#create a udp socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
while True:
	message = raw_input('-->')
	clientSocket.sendto(message,(serverName,serverPort))
	modifiedMessage,serverAddress = clientSocket.recvfrom(2048)
	print modifiedMessage
clientSocket.close()
