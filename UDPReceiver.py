"""
    Simple UDP socket server
"""

from socket import *
import sys
import select

host = ""
port = 9999

s = socket(AF_INET, SOCK_DGRAM)
s.bind((host, port))

addr = (host, port)
buffer = 1024

data,addr = s.recvfrom(buffer)
print("Received File: " + data.strip())

f = open(data.strip(), 'wb')

data,addr = s.recvfrom(buffer)

try:
    while(data):
        f.write(data)
        s.settimeout(2)
        data,addr = s.recvfrom(buffer)
except timeout:
    f.close()
    s.close()
    print("File downloaded")