# -*- coding: utf-8 -*-
import re
import rsa
import socket
from ServerC import *


class ClientB:
    def __init__(self, name='client_b', ip='127.0.0.1', port=6666, **kwargs):
        assert re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
                        , ip), "IP address invalid"
        self.name = name
        self.ip = ip
        self.port = port
        self.ca = ServerC()
        self._privkey = self.ca.gen_newkeys(self.name)
        assert self._privkey, "Failed to generate keys"
        self.start_client()

    def start_client(self):
        sock = socket.socket()
        sock.connect((self.ip, self.port))
        print('Successfully connect {}:{}'.format(self.ip, self.port))
        while True:
            # send data
            send_cache = input("Input> ")
            pubkey = self.ca.get_pubkey('client_a')
            if pubkey:
                send_data = rsa.encrypt(send_cache.encode(), pubkey)
            else:
                print("Failed to encrypt.")
                sock.close()
                exit()
            sock.sendall(send_data)
            if send_cache == 'bye':
                break
            # receive data
            # accept_data = str(sock.recv(1024), encoding='utf8')
            accept_data = sock.recv(1024)
            accept_data = rsa.decrypt(accept_data, self._privkey).decode()
            print("Receive: ", accept_data)
        sock.close()

client_b = ClientB()
