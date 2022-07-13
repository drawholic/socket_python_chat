import json
from utils import Server

my_server = Server()

while True:

    conn, addr, data = my_server.accept()

    if data['type'] == 'NAME':
        client = my_server.add_client(addr, data)
        new_user_message = f'New user: {data["data"]}'
        print(new_user_message)
        conn.send(json.dumps(new_user_message).encode())

    elif data['type'] == 'TEXT':
        message = my_server.print_message(addr)
        print(message)
        conn.sendall(json.dumps(message).encode())
