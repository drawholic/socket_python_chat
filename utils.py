import socket
import json


def send_name(client: socket.socket):
    name = input('Enter your name: ')
    info = {
        'type': 'NAME',
        'data': name
    }

    client.sendall(json.dumps(info).encode())


def send_text(client: socket.socket):
    text = input('Enter your message: ')
    info = {
        'type':'TEXT',
        'data':text
    }


class Server:

    def __init__(self):
        self.server = socket.socket()
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind(('', 9090))
        self.server.listen(5)
        self.clients = []
        print('[:]____HELLO, CHAT STARTED TO WORK____[:]')

    def accept(self):
        conn, addr = self.server.accept()
        data = conn.recv(1024)
        data = json.loads(data.decode())
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

    def print_message(self, addr):
        user = {}
        for client in self.clients:
            if client['addr'] == addr:
                user = client
        text = self.accept()[2]
        message = f'[{user["name"]}: {text}]'
        return message


