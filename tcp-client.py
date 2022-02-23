import socket

# define targets as feanor.xyz
target_host="www.feanor.xyz"
target_port=80

# instantiating a socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connecting
client.connect((target_host, target_port))

# send data
client.send(b"GET / HTTP/1.1\r\nHost: feanor.xyz\r\n\r\n")

# recieve data
response = client.recv(4096)

# print the response
print(response.decode())

#close the connection
client.close()