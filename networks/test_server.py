from socket import *
import threading


s = socket(AF_INET, SOCK_STREAM)
s.bind(("", 9000))
s.listen(5)
clients = []

print("Server started!")


def client(c, a):
    print(f"received connection from {a}")
    while True:
        data = c.recv(1000)
        print(data)
        if data == b"":
            print(data)
            c.send(b"You have left the chat!")
            print(f"{a} has left the chat!")
            c.close()
            break
        if c.fileno() != -1:
            print("updating")
            print(c.fileno())
            update_chat(data)
        print(data.decode("utf-8"))


def update_chat(msg):
    for c in clients:
        c.send(msg)


while True:
    c, a = s.accept()
    clients.append(c)
    x = threading.Thread(target=client, args=(c, a))
    x.start()
