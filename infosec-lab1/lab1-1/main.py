# -*- coding:utf-8 -*-
import os, re
from MyAES import *
"""
Using different mode in AES to encrypt a bmp image.
But it doesn't support decrypt yet...
"""

LOG_PATH = './aes.log'
OUT_DIR = './images/'
IMG_PATH = './images/lena512.bmp'
KEY = 'keyskeyskeyskeys'
MODE_LIST = ['ECB', 'CBC', 'CFB', 'OFB', 'CTR']


def test(key, mode):
    # testing for encrypt/decrypt text
    my_aes = MyAES(key, mode)
    e = my_aes.encrypt(text='0123456789ABCDEF')
    print(e)
    d = my_aes.decrypt(e)
    print(d)


def encrypt():
    # Encrypt the bmp image using different modes
    for mode in MODE_LIST:
        print('[+]{} mode'.format(mode))
        my_aes = MyAES(KEY, mode, img_clr=IMG_PATH)
        my_aes.encrypt(img_out=os.path.join(OUT_DIR, '{}_out.bmp'.format(mode)))


def main():
    if os.path.isfile(LOG_PATH):
        os.remove(LOG_PATH)
    for file in os.listdir(OUT_DIR):
        if re.match(r'.*_out.bmp', file):
            os.remove(os.path.join(OUT_DIR, file))
    encrypt()

if __name__ == '__main__':
    main()
