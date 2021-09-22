import socket

msgfromclient = "hello udp server"

bytesTosend = str.encode(msgfromclient)

serverAddressPort = ('127.0.0.1', 20001)
buffersize = 1024

UDPCLIENTSOCKET = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPCLIENTSOCKET.sendto(bytesTosend, serverAddressPort) #2

msgfromserver = UDPCLIENTSOCKET.recvfrom(buffersize) #3
msg = "message from server {}".format(msgfromserver[0])

print(msg)