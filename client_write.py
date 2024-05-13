import socket
import time
import threading

# IP ADDRESS AND PORT NUMBER for the first server
server_ip = '127.0.0.1'
server_port = 5000

# TCP/IP SOCKET
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to the server
client_socket.connect((server_ip, server_port))

def create_message(addr, val):
    return "WRITE*{}*{}".format(addr, val)

def send_message(client_socket, addr, val):
    message = create_message(addr, val)
    client_socket.sendall(message.encode())
    print(f"Sending message: {message}")
    response = client_socket.recv(1024)
    print(f"Server response: {response.decode()}")

def send_multiple_messages(client_socket):
    while True:
        time.sleep(1)
        send_message(client_socket, 23, 45)
        time.sleep(1)
        send_message(client_socket, 23, 39)
        time.sleep(1)
        send_message(client_socket, 23, 50)

send_multiple_messages(client_socket)

   
