import socket
import sys

def sender():
    msgFromClient = "Hello it's Tom"
    bytesToSend = str.encode(msgFromClient)
    serverAddressPort = ("192.168.1.207", 11000)
    bufferSize = 1024

    UDPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    UDPClientSocket.connect(serverAddressPort)

    UDPClientSocket.send(msgFromClient.encode('utf-8'))
sender()