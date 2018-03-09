# -*- coding:utf-8 -*-
from Crypto import Random
from AESEncrypt import AESEncrypt


def test(key, mode):
    my_aes = AESEncrypt(key, mode)
    e = my_aes.encrypt('0123456789ABCDEF')
    print(e)
    d = my_aes.decrypt(e)
    print(d)

if __name__ == '__main__':
    key = 'keyskeyskeyskeys'
    mode = 'CTR'
    # ['ECB', 'CBC', 'CFB', 'OFB', 'CTR']
    # my_aes = AESEncrypt(key, mode, img_clr='./lena512.bmp')
    # my_aes.encrypt(img_out='CBC_out.bmp')
    test(key, mode)
