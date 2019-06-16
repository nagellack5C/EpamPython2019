from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(("", 9000))
s.listen(5)
while True:
    c, a = s.accept()
    msg = c.recv(1024)
    print(c)
    print(a)
    print(msg.decode("utf-8"))
    c.close()