from socket import *
import threading
import sys


class Server:

    def __init__(self):
        self.clients = {}

    def client(self, c, a, id):
        print(f"received connection from {a}")
        while True:
            data = c.recv(1000)
            if data == b"\\quit\\":
                c.send(b"\\You have left the chat!\\")
                print(f"{a} has left the chat!")
                c.close()
                self.clients.pop(id)
                break
            if c.fileno() != -1:
                data = str(data, encoding="utf-8")
                self.update_chat(data, c.getpeername()[1])

    def update_chat(self, msg, port):
        print(f"{port}: {msg}")
        for id in self.clients:
            self.clients[id].send(bytes(f"{port}: {msg}", encoding="utf-8"))

    def server(self, port):
        s = socket(AF_INET, SOCK_STREAM)
        s.bind(("", port))
        s.listen(5)
        print("Server started!")
        while True:
            c, a = s.accept()
            id = c.getpeername()
            self.clients[id] = c
            x = threading.Thread(target=self.client, args=(c, a, id))
            x.start()


server = Server()
server.server(int(sys.argv[1]))
