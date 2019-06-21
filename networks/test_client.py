from socket import *
import time
import threading
# import q



def start_client():
    cl_s = socket(AF_INET, SOCK_STREAM)
    cl_s.connect(("", 9000))
    return cl_s

def chatter(socket):
    while True:
        msg = input("Your message: ")
        socket.send(bytes(msg, encoding="utf-8"))
        if msg == "":
            socket.close()
            break

# def start_chat(socket):
#     while True:
#         msg = input("Your message: ")
#         # print(socket)
#         # sleep(5)
#         # print(socket)
#         # data = cl_s.recv(10000)
#     # print(data)
#     cl_s.close()


chatter(start_client())
