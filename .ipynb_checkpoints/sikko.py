import socket
import time
import threading

# IP ADDRESS AND PORT NUMBER for the first server
server_ip = '127.0.0.1'
server_port = 5000

# IP ADDRESS AND PORT NUMBER for the second server
server_ip_2 = '127.0.0.1'
server_port_2 = 5008

# Flag to control whether the first client should continue running
first_client_running = True

def first_client():
    global first_client_running
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
        while first_client_running:
            time.sleep(1)
            send_message(client_socket, 23, 45)
            time.sleep(1)
            send_message(client_socket, 23, 39)
            time.sleep(1)
            send_message(client_socket, 23, 50)

    # Call send_multiple_messages function in a loop
    send_multiple_messages(client_socket)
    # Close the client socket when done
    client_socket.close()

# Create a thread for the first_client function
first_client_thread = threading.Thread(target=first_client)

def sec_client():
    # TCP/IP SOCKET FOR THE SECOND SERVER
    client_socket_2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect to the second server
    client_socket_2.connect((server_ip_2, server_port_2))
    while True:
        response = client_socket_2.recv(1024)
        response_sec = response.decode('utf-8')
        if response_sec == 'start':
            # If the second server sends "start" message, start the first client thread
            first_client_thread.start()
        elif response_sec == 'stop':
            # If the second server sends "stop" message, stop the first client thread
            global first_client_running
            first_client_running = False
            # Wait for the first client thread to finish
            first_client_thread.join()
            # Close the client socket for the second server
            client_socket_2.close()

# Start the second client directly since we are already in a thread
sec_client()
