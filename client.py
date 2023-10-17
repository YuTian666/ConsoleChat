import socket
import threading

def send_message(client_socket):
    while True:
        message = input("Chat >> ")
        client_socket.send(message.encode())

def receive_message(client_socket):
    while True:
        data = client_socket.recv(1024).decode()
        print(f"Get Message --> ({data})")

def RunClient(ip,post):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_host = ip
    server_port = post
    client_socket.connect((server_host, server_port))
    send_thread = threading.Thread(target=send_message, args=(client_socket,))
    receive_thread = threading.Thread(target=receive_message, args=(client_socket,))
    send_thread.start()
    receive_thread.start()