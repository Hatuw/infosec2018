# -*- coding:utf-8 -*-
import os
from AESEncrypt import AESEncrypt


def test(key, mode):
    my_aes = AESEncrypt(key, mode)
    e = my_aes.encrypt(text='0123456789ABCDEF')
    print(e)
    d = my_aes.decrypt(e)
    print(d)

if __name__ == '__main__':
    if os.path.isfile('./aes.log'):
        os.remove('./aes.log')
    key = 'keyskeyskeyskeys'
    mode = 'ECB'
    mode_list = ['ECB', 'CBC', 'CFB', 'OFB', 'CTR']
    for mode in mode_list:
        print('[+]{} mode'.format(mode))
        # test(key, mode)
        my_aes = AESEncrypt(key, mode, img_clr='./images/lena512.bmp')
        my_aes.encrypt(img_out='./images/{}_out.bmp'.format(mode))