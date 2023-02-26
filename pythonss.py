import socket
from socket import getaddrinfo
var=getaddrinfo(None,53,0,socket.SOCK_DGRAM,0,socket.AI_PASSIVE)
print(var)
