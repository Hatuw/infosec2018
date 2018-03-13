# -*- coding: utf-8 -*-
import re
import rsa
import socket
from ServerC import *


class ClientA:
    def __init__(self, name='client_a', ip='127.0.0.1', port=6666, **kwargs):
        assert re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
                        , ip), "IP address invalid"
        self.name = name
        self.ip = ip
        self.port = port
        self.ca = ServerC()
        self._privkey = self.ca.gen_newkeys(self.name)
        assert self._privkey, "Failed to generate keys"
        self.start_server()

    def start_server(self):
        sock = socket.socket()
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((self.ip, self.port))
        sock.listen(5)
        print('Client A start at {}:{}'.format(self.ip, self.port))
        # begin to talk
        conn, addr = sock.accept()
        while True:
            # accept_data = str(conn.recv(1024), encoding='utf8')
            accept_data = conn.recv(1024)
            accept_data = rsa.decrypt(accept_data, self._privkey).decode()
            print("Receive: ", accept_data)
            if accept_data == 'bye':
                break
            send_data = input("Reply> ")
            pubkey = self.ca.get_pubkey('client_b')
            if pubkey:
                send_data = rsa.encrypt(send_data.encode(), pubkey)
            else:
                print("Failed to encrypt.")
                sock.close()
                exit()
            conn.sendall(send_data)
        conn.close()
        sock.close()

client_a = ClientA()