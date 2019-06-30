from socket import *
import time
import threading
import sys
import os


class Client:

    def __init__(self, port):
        self.port = port
        self.c_socket = None
        self.id = None

    def start(self):
        self.c_socket = self.connect(self.port)
        self.id = str(self.c_socket.getsockname()[1])
        print("Start typing")
        chtr = threading.Thread(target=self.chatter)
        rcvr = threading.Thread(target=self.receiver)
        chtr.start()
        rcvr.start()

    def connect(self, port):
        c_socket = socket(AF_INET, SOCK_STREAM)
        c_socket.connect(("", port))
        return c_socket

    def chatter(self):
        while True:
            msg = input()
            if msg == "":
                self.c_socket.send(b"\\quit\\")
                print("quitting...")
                break
            self.c_socket.send(bytes(msg, encoding="utf-8"))

    def receiver(self):
        while True:
            data = self.c_socket.recv(1000)
            if data == b"\\You have left the chat!\\":
                break
            data = str(data, encoding="utf-8")
            if self.id not in data:
                print(data)


port = int(sys.argv[1])
client = Client(port)
client.start()