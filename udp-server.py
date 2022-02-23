import socket
import threading

IP = "0.0.0.0"
PORT = 9997

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((IP, PORT))
    print(f"[*] Listening on {IP}:{PORT}")

    while True:
        data, addr = server.recvfrom(1024)
        print(f"[*] Recieved from {addr}: {data}")

if __name__=="__main__":
    main()
