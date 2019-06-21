from socket import *



s = socket(AF_INET, SOCK_STREAM)
s.bind(("", 9000))
s.listen(5)

print("Server started!")
c, a = s.accept()
print(f"received connection from {a}")
while True:
    data = c.recv(1000)
    if not data:
        break
    print(data.decode("utf-8"))