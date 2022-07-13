import socket
from utils import send_name

client = socket.socket()
client.connect(('localhost', 9090))

send_name(client)
answer = client.recv(1024).decode()
print(answer)

while True:

    data = input('Enter your text: ')
    if data == 'q':
        client.close()
        break
    data = data.encode()
    client.sendall(data)
    data = client.recv(1024)
    data = data.decode()
    print('received', data)

#
# client.send('hello worlds'.encode())
#
# data = client.recv(1024)
# client.close()
# print(data)