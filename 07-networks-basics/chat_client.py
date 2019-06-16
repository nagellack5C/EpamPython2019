from socket import *
s = socket(AF_INET, SOCK_STREAM)
s.connect(("127.0.0.1", 9000))
msg = input("Enter message: ")
s.send(bytes(msg, encoding="utf-8"))
data = s.recv(10000)
s.close()