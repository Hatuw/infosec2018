# 实验一 密码算法实验

整体完成情况:
- [x] 1.1 分组密码算法AES及操作模式实验
- [ ] 1.2 公钥密码算法RSA

## Requirement
- Python3.5
- Python packages:
	*you can use* `pip install <package name>` *to install it.*
    - Crypto
    - binascii

(**Only test on Ubuntu16.0.4LTS**. If you run this code in other enviroment, some bugs may appear.)

## 1.1 分组密码算法AES及操作模式实验
本次实验采用AES-128位对图片进行加密,分别采用 `'ECB', 'CBC', 'CFB', 'OFB', 'CTR'` 模式,对比不同加密模式下的加密效果.实验详细要求参考[这里](./实验1  密码算法实验.doc)

完成情况:

- [x] 电子密码本模式 ECB
- [x] 密码分组链接 CBC
- [x] 密码反馈 CFB
- [x] 输出反馈 OFB
- [x] 计数器模式 CTR
- [x] 日志功能

主要实现函数为 `main.py` ,实现AES加密的主类为 `AESEncrypt`, 代码还没整理好, Welcome to pull request~

运行方法:
`'ECB', 'CBC', 'CFB', 'OFB'` 下只需定义key和mode即可,如加密文本:
``` Python
>> from AESEncrypt import AESEncrypt
>> key = 'keyskeyskeyskeys'
>> mode = 'ECB'
>> my_aes = AESEncrypt(key, mode)
>> e = my_aes.encrypt('0123456789ABCDEF') # 加密
>> print(e)
b'6c59fd98f9dc860064413899bd301b43'
>> d = my_aes.decrypt(e) # 解密
>> print(d)
b'0123456789ABCDEF'
```
日志生成在`./aes.log`,有需要的自己分析

## 1.2 公钥密码算法RSA

- [ ] 编写生成一对RSA密钥的程序
- [ ] 生成实验用的128位信息
- [ ] 设计对自己生成的密钥进行测试的方法
- [ ] 设计对别人生成的密钥进行测试的方法
- [ ] 完成各个角色的测试