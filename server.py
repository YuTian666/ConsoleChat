import socket
import threading
online_clients = {} #连接的字典
helps = '''
SEND [IP] [MSG]
You can try : send [ip] Hello!
The [IP] will get "Hello!".

GROUP [MSG]
You can try : group Hello!
All IP(and you) can get "Hello!".

SEE
You can try : SEE
You can get all online ip.

find [IP]
You can try : find [IP]
You get the [IP] is Yes or No online.
'''
def handle_client(client_socket, client_address):
    while True:
        try:
            data = client_socket.recv(1024).decode()
            if not data:
                print(f"与 {client_address} 的连接已关闭。")
                break
            
            command = data.split()
            print(f"{client_address} >> ",end = "")
            for i in command:
                print(i,end = " ")
            print("")
            if command[0] == "send":
                target_ip = command[1]
                message = ' '.join(command[2:])
                if target_ip in online_clients:
                    target_socket = online_clients[target_ip]
                    target_socket.send(message.encode())
                else:
                    client_socket.send(f"Client {target_ip} isn't online.".encode())
            elif command[0] == "group":
                message = ' '.join(command[1:])
                for ip, socket in online_clients.items():
                    socket.send(message.encode())
            elif command[0] == "see":
                online_ips = ', '.join(online_clients.keys())
                client_socket.send(f"Online IP: {online_ips}".encode())
            elif command[0] == "find":
                target_ip = command[1]
                if target_ip in online_clients:
                    client_socket.send(f"Client {target_ip} is online.".encode())
                else:
                    client_socket.send(f"Client {target_ip} isn't online.".encode())
            elif command[0] == "help":
                client_socket.send(helps.encode())
            else:
                client_socket.send(f"Is not a command!You can try input help".encode())
        except Exception as e:
            print(f"处理客户端 {client_address} 时出错：{str(e)}")
            break
def RunServer(ip,post):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_host = ip
    server_port = post
    server_socket.bind((server_host, server_port))
    server_socket.listen(5)
    print(f"The friend code is:\nCopy --> client {server_host} {server_port}")
    print(f"Server is LISTEN >>  {server_host}:{server_port}")
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"接受来自 {client_address} 的连接")
        online_clients[client_address[0]] = client_socket
        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_handler.start()
