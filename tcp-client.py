import socket

# define targets as feanor.xyz
target_host = "0.0.0.0"
target_port = 9998

# instantiating a socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connecting
client.connect((target_host, target_port))

# send data
client.send(b"Hello, Friend.")

# recieve data
response = client.recv(4096)

# print the response
print(response.decode())

# close the connection
client.close()
