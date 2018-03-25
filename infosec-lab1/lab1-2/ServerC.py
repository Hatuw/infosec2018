# -*- coding:utf-8 -*-
import os
import re
import rsa

KEY_STORE = './keystore'
if not os.path.exists(KEY_STORE):
    os.mkdir(KEY_STORE)


class ServerC:
    def __init__(self):
        pass

    def gen_newkeys(self, uname):
        """
        Generate keys and return once.
        :param uname: user name
        :return: privkey: private key
        """
        # !!! The private key will send to clinet only once.
        key_files = os.listdir(KEY_STORE)
        for key_file in key_files:
            if re.match(uname, key_file):
                return False
        # use rsa lib to generate keys
        (pubkey, privkey) = rsa.newkeys(1024)

        # store keys
        with open(os.path.join(KEY_STORE, '{}_public.pem'.format(uname)), 'w') as f:
            f.write(pubkey.save_pkcs1().decode())

        with open(os.path.join(KEY_STORE, '{}_private.pem'.format(uname)), 'w') as f:
            f.write(privkey.save_pkcs1().decode())

        return privkey

    def get_pubkey(self, uname):
        """
        Get public key
        :param uname: username
        :return: pubkey: public key
        """
        key_path = os.path.join(KEY_STORE, '{}_public.pem'.format(uname))
        if os.path.exists(key_path):
            with open(key_path) as f:
                pubkey = rsa.PublicKey.load_pkcs1(f.read().encode())
            return pubkey
        else:
            return False
