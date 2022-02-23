import socket

# define target as feanor.xyz
target_host = "0.0.0.0"
target_port = 9997

# instantiate a socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send data
client.sendto(b"Hello, friend.", (target_host, target_port))

# recieve data on localhost
data, addr = client.recvfrom(4096)

# print the data
print(data.decode())

# close the connection
client.close()
