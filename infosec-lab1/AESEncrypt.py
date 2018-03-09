# -*- coding: utf-8 -*-
import os
import random
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex, hexlify, unhexlify


class AESEncrypt:
    """ This class is used to inference AES encrypt algorithm.
    Note: It only used to encrypt a bmp image, never test on
    other plain-text
    It include: ['ECB', 'CBC', 'CFB', 'OFB', 'CTR'] mode
        EBC mode:
        CBD mode:
        CFB mode:
        OFB mode:
        CTR mode:
    """
    def __init__(self, key, mode, img_clr=None):
        assert len(key) == 16, 'key must be 16 bytes in AES-128'
        self.key = key
        assert mode in ['ECB', 'CBC', 'CFB', 'OFB', 'CTR'], 'aes mode not support yet~'
        self.mode = eval('AES.MODE_{}'.format(mode))
        self.ciphertext = ''
        self.img_clr = img_clr
        if self.img_clr:
            self.img_clr = img_clr
            self.__get_header__()

    def __get_sizes__(self, dibheader):
        # Get image's dimensions (at offsets 4 and 8 of the DIB header)
        DIBheader = []
        for i in range(0, 80, 2):
            DIBheader.append(int(hexlify(dibheader)[i:i + 2], 16))
        self.width = sum([DIBheader[i + 4] * 256 ** i for i in range(0, 4)])
        self.height = sum([DIBheader[i + 8] * 256 ** i for i in range(0, 4)])

    def __get_header__(self):
        """
        Read BMP and DIB headers from input image and write them to output image
        """
        with open(self.img_clr, 'rb') as f_in:
            # BMP is 14 bytes
            bmpheader = f_in.read(14)
            # DIB is 40 bytes
            dibheader = f_in.read(40)
            self.__get_sizes__(dibheader)
            self._bmpheader = bmpheader
            self._dibheader = dibheader

    def encrypt(self, text=None, **kwargs):
        if self.img_clr:
            if 'img_out' in kwargs:
                img_out = kwargs['img_out']
            else:
                img_out = 'test_out.bmp'
            with open(self.img_clr, 'rb') as f_in:
                with open(img_out, 'wb') as f_out:
                    f_out.write(self._bmpheader)
                    f_out.write(self._dibheader)
                    row_padded = (self.width * self.height * 3)
                    image_data = f_in.read(row_padded)
                    cleartext = unhexlify(hexlify(image_data))
                    length = 16
                    count = len(cleartext)
                    if (count % length) != 0:
                        # padding
                        add = length - (count % length)
                    else:
                        add = 0
                    cleartext += (b'\0' * add)

                    # Initialization Vector
                    IV = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
                    print(IV)
                    print(len(IV))
                    # Encryptor
                    encryptor = AES.new(self.key, self.mode, IV=IV)
                    # Perform the encryption and write output to file
                    f_out.write(encryptor.encrypt(cleartext))
        else:
            if self.mode in [AES.MODE_ECB, AES.MODE_CBC, AES.MODE_CFB, AES.MODE_OFB]:
                cryptor = AES.new(self.key, self.mode, self.key)
            elif self.mode == AES.MODE_CTR:
                secret = os.urandom(16)
                cryptor = AES.new(self.key, self.mode, self.key, counter=lambda: secret)
            # key must be 16(AES-128) / 24(AES-192) / 32(AES-256) bytes
            length = 16
            count = len(text)
            if (count % length) != 0:
                # padding
                add = length - (count % length)
            else:
                add = 0
            text += ('\0' * add)
            self.ciphertext = cryptor.encrypt(text)
            return b2a_hex(self.ciphertext)

    def decrypt(self, text, **kwargs):
        if self.mode in [AES.MODE_ECB, AES.MODE_CBC, AES.MODE_CFB, AES.MODE_OFB]:
            cryptor = AES.new(self.key, self.mode, self.key)
            plain_text = cryptor.decrypt(a2b_hex(text))
        elif self.mode == AES.MODE_CTR:
            secret = os.urandom(16)
            cryptor = AES.new(self.key, self.mode, self.key, counter=lambda: secret)
            plain_text = cryptor.decrypt(a2b_hex(text))
        return plain_text.rstrip(b'\0')
