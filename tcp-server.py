import socket
import threading

# define IP and port to listen on
IP = "0.0.0.0"
PORT = 9998


def main():
    # handler function
    def handle_client(client_socket):
        # use the input socket as socket
        with client_socket as sock:
            # recieve the request
            request = sock.recv(1024)

            # print status and message in UTF-8 encoding
            print(f'[*] Recieved: {request.decode("utf-8")}')

            # send back an ACK packet for handshake
            sock.send(b"ACK")

    # instantiate a socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind to a port
    server.bind((IP, PORT))

    # listen on that port with a backlog of maximum of 5 connections
    server.listen(5)

    # print current status
    print(f"[*] Listening on {IP}:{PORT}")

    # when something is heard/recieved
    while True:
        # accept the incoming connection
        client, address = server.accept()

        # print current status
        print(f"[*] Accepted connection from {address[0]}:{address[1]}")

        # create a handler thread
        client_handler = threading.Thread(target=handle_client, args=(client,))

        # start the handler
        client_handler.start()


if __name__ == "__main__":
    main()
