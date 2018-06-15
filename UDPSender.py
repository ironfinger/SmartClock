import socket
import sys

def sender():
    msgFromClient = "Hello it's Tom"
    bytesToSend = str.encode(msgFromClient)
    serverAddressPort = ("", "11000")
    bufferSize = 1024

    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    UDPClientSocket.sendto(bytesToSend, serverAddressPort)

    msgFromServer = UDPClientSocket.recvfrom(bufferSize)

    msg = "Message from server {}",format(msgFromServer[0])