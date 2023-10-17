import server
import client
def Run():
    while True:
        answer = input("Input you command >> ")
        com = answer.split()
        if answer == "server":
            ip = input("ChatServer ready RUN!.\nPlease input your IP(format=xx.xx.xx.xx) >> ")
            post = int(input("Please input your post(Is a num,you can input:12345) >> "))
            server.RunServer(ip,post)
        elif answer == "client":
            ip = input("You are client.\nPlease input IP(Format = xx.xx.xx.xx) >> ")
            post = int(input("Please input post(Format = Is a num) >> "))
            client.RunClient(ip,post)
        elif answer == "help":
            print("The writer is YuTian -> https://yutianqwq.top/")
            print("You can using 'Windows Terminal' is really great!!!")
            print("This console command:")
            print("server \nclient \nhelp")
            print("you can input [client+ip+post] such as : client 127.0.0.1 8888")
        elif com[0] == "client":
            client.RunClient(com[1],int(com[2]))
        else:
            print("Want to see other information???")