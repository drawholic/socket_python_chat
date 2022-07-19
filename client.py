import json
import socket
from utils import Client

client = socket.socket()
client.connect(('localhost', 9090))


answer = client.recv(1024).decode()
print(answer)

while True:
    try:
        client.sendall(json.dumps(info).encode())
    except Exception as e:
        print(e)