# -*- coding: utf-8 -*-
import os
import re
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex, hexlify, unhexlify


class MyAES:
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
        self.mode_str = 'AES.MODE_{}'.format(mode)
        self.mode = eval(self.mode_str)
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

    def __padding__(self, cleartext):
        length = 16
        count = len(cleartext)
        if (count % length) != 0:
            # padding
            add = length - (count % length)
        else:
            add = 0
        if self.img_clr:
            cleartext += (b'\0' * add)
        else:
            cleartext += ('\0' * add)
        return cleartext

    def __get_counter__(self, filename='aes.log'):
        with open(filename, 'r') as f_in:
            logs_data = f_in.readlines()
        for line in logs_data:
            if re.match(r'.*secret=(.*)\n', line):
                result = re.findall(r'secret=(.+)\n', line)[0]
                return eval(result)
        return False

    def __log__(self, mode, key, **kwargs):
        with open('aes.log', 'a+') as f_in:
            format_log = '[{}]:\n\tkey={}'.format(mode, key)
            f_in.write(format_log)
            for key, value in kwargs.items():
                if value:
                    f_in.write('\n\t{}={}'.format(key, value))
            f_in.write('\n')

    def encrypt(self, **kwargs):
        if self.img_clr:
            # encrypt an image
            img_out = kwargs['img_out'] if 'img_out' in kwargs else './images/test_out.bmp'
            with open(self.img_clr, 'rb') as f_in:
                with open(img_out, 'wb') as f_out:
                    f_out.write(self._bmpheader)
                    f_out.write(self._dibheader)
                    row_padded = (self.width * self.height * 3)
                    image_data = f_in.read(row_padded)
                    cleartext = unhexlify(hexlify(image_data))
                    cleartext = self.__padding__(cleartext)

                    # Initialization Vector
                    # IV = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
                    # Create a cryptor
                    if self.mode in [AES.MODE_ECB, AES.MODE_CBC, AES.MODE_CFB, AES.MODE_OFB]:
                        secret = ''
                        cryptor = AES.new(self.key, self.mode, IV=self.key)
                    elif self.mode == AES.MODE_CTR:
                        secret = os.urandom(16)
                        cryptor = AES.new(self.key, self.mode,
                                          IV=self.key, counter=lambda: secret)
                    # Perform the encryption and write output to file
                    self.__log__(self.mode_str, self.key,
                                 **{'secret': secret})
                    f_out.write(cryptor.encrypt(cleartext))
        elif 'text' in kwargs:
            cleartext = kwargs['text']
            # encrypt a text
            # key must be 16(AES-128) / 24(AES-192) / 32(AES-256) bytes
            cleartext = self.__padding__(cleartext)
            # Create a cryptor
            if self.mode in [AES.MODE_ECB, AES.MODE_CBC, AES.MODE_CFB, AES.MODE_OFB]:
                secret = ''
                cryptor = AES.new(self.key, self.mode, IV=self.key)
            elif self.mode == AES.MODE_CTR:
                secret = os.urandom(16)
                cryptor = AES.new(self.key, self.mode,
                                  IV=self.key, counter=lambda: secret)
            self.ciphertext = cryptor.encrypt(cleartext)
            self.__log__(self.mode_str, self.key,
                         **{'secret': secret,
                            'cleartext': cleartext,
                            'ciphertext': b2a_hex(self.ciphertext)})
            return b2a_hex(self.ciphertext)

    def decrypt(self, text, **kwargs):
        if self.mode in [AES.MODE_ECB, AES.MODE_CBC, AES.MODE_CFB, AES.MODE_OFB]:
            cryptor = AES.new(self.key, self.mode, self.key)
            plain_text = cryptor.decrypt(a2b_hex(text))
        elif self.mode == AES.MODE_CTR:
            secret = self.__get_counter__()
            assert secret, 'CTR mode must include args `counter(secret)`'
            cryptor = AES.new(self.key, self.mode,
                              self.key, counter=lambda: secret)
            plain_text = cryptor.decrypt(a2b_hex(text))
        return plain_text.rstrip(b'\0')
