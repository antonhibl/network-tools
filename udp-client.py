import socket

# define target as feanor.xyz
target_host = "104.168.243.128"
target_port = 80

# instantiate a socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send data
client.sendto(b"GET / HTTP/1.1\r\nHost: feanor.xyz\r\n\r\n", (target_host, target_port))

# recieve data on localhost
data, addr = client.recvfrom(4096)

# print the data
print(data.decode())

# close the connection
client.close()
