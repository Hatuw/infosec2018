# -*- coding:utf-8 -*-
import re
import rsa
import json
import socket

class Server_C:
    def __init__(self, ip='127.0.0.1', port=6666, **kwargs):
        assert re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
                        , ip), "IP address invalid"
        self.ip = ip
        self.port = port

    def json_format(self, dict_data):
        return json.dumps(dict_data)

    def genkeys(self):
        (pubkey, privkey) = rsa.newkeys(1024)
        pubkey = {
            'n': pubkey.n,
            'e': pubkey.e
        }
        privkey = {
            'n': privkey.n,
            'p': privkey.p,
            'q': privkey.q,
            'd': privkey.d,
            'e': privkey.e
        }
        pubkey = self.json_format(pubkey)
        privkey = self.json_format(privkey)
        return pubkey, privkey

    def setkeys(self, **kwargs):
        """
        This function is used to set keys and keys' owner
        :param kwargs:
         pubkey, privkey, owner, vercode
        :return: bool, Success or not
        """
        pass

    def start_server(self):
        sock = socket.socket()
        sock.bind((self.ip, self.port))
        sock.listen(5)
        print('Server C open. Listing at: {}:{}'.format(self.ip, self.port))
        pubkey, privkey = self.genkeys()
        while True:
            conn, addr = sock.accept()
            data = conn.recv(2048)
            print(str(data, 'utf-8'))
            conn.send(pubkey, 'utf8')
            conn.close()
            sock.close()


def test():
    server_c = Server_C()
    pubkey, privkey = server_c.genkeys()
    server_c.start_server()

test()
