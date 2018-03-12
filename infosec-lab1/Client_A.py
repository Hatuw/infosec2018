# -*- coding: utf-8 -*-
import re
import json
import socket

class Client_A:
    def __init__(self, ip='127.0.0.1', port=6666, **kwargs):
        assert re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
                        , ip), "IP address invalid"
        self.ip = ip
        self.port = port

    def start_client(self):
        sock = socket.socket()
        sock.connect((self.ip, self.port))
        sock.sendall(bytes('I am client A, please generate keys for me, tks~', 'utf8'))
        server_reply = sock.recv(4096)
        keys = json.loads(server_reply)
        print(keys)
        # print(str(server_reply, 'utf8'))


def test():
    client_a = Client_A()
    client_a.start_client()

test()
