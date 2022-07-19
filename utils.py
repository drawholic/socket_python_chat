import socket
import json


class Client:
    def __init__(self, username):
        self.client = socket.socket()
        self.client.connect(('localhost', 9090))
        self.username = username
        self.client.sendall(b'')

    def send_message(self, message):
        data = {
            'username':self.username,
            'message':message
        }
        data = json.dumps(data).encode()
        self.client.sendall(data)


class Server:

    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.server.setsockopt(socket.AF_INET, socket.SOCK_STREAM, 1)
        self.server.bind(('', 9090))
        self.server.listen(5)
        self.clients = []
        print('[:]____HELLO, CHAT STARTED TO WORK____[:]')

    def accept(self):
        conn, addr = self.server.accept()
        data = conn.recv(1024)
        data = json.loads(data.decode())
        print('accepted')
        return conn, addr, data

    def client(self):
        pass

    def add_client(self, addr, data):
        client = {
            'name': data['data'],
            'addr': addr,
            'host': addr[0],
            'port': addr[1]
        }
        self.clients.append(client)
        return client['name']

    def print_message(self, addr, data):
        user = {}
        print('got message')
        for client in self.clients:
            if client['addr'] == addr:
                user = client
                # print('got user')
        text = data['data']
        # print('hey from here')
        # print(text)
        message = f'[{user["name"]}: {text}]'
        return message


