# 实验一 密码算法实验

整体完成情况:
- [x] 1.1 分组密码算法AES及操作模式实验
- [x] 1.2 公钥密码算法RSA


## Requirement
- Ubuntu16.04.4 LTS
- Python3.5.2
- Python packages:

	*you can use* `pip install <package name>` *to install it.*
    - exb 1.1
        - Crypto
        - binascii
	- exb 1.2
		- re
		- rsa
		- socket

(**Only test on Ubuntu16.0.4LTS**. If you run this code in other enviroment, such as Windows, some bugs may appear.)

## 1.1 分组密码算法AES及操作模式实验
本次实验采用AES-128位对图片进行加密,分别采用 `'ECB', 'CBC', 'CFB', 'OFB', 'CTR'` 模式,对比不同加密模式下的加密效果.实验详细要求参考[这里](../实验1  密码算法实验.doc)

完成情况:

- [x] 电子密码本模式 ECB
- [x] 密码分组链接 CBC
- [x] 密码反馈 CFB
- [x] 输出反馈 OFB
- [x] 计数器模式 CTR
- [x] 日志功能

Run in different mode:

 - `'ECB', 'CBC', 'CFB', 'OFB'` 下只需定义key和mode即可.
 - `'CTR'` 模式需定义 `counter` 默认为 `counter = lambda: os.urandom(16)`

Demo:
``` Python
>> from AESEncrypt import *
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
详见`main.py`,日志生成在`./aes.log`,有需要的自己分析日志和源码.

***

## 1.2 公钥密码算法RSA

> 模拟实现128位信息的加密通信过程。
 - 实验由3人一组共同完成：
 	- 第一人与第二人之间进行128位信息的加密交换。
 	- 第三人负责为第一人和第二人各生成一对公私钥对，并分别把对应的私钥传给第一人和第二人，并把他们的公钥公开。
 - 进行一轮实验后，轮转角色，使每一人都承担一次密钥生成的角色、报文发送角色和报文接收角色，担当每一种角色时，运行自己设计的该角色的程序。

- [x] 编写生成一对RSA密钥的程序
- [x] 生成实验用的128位信息
- [x] 设计对自己生成的密钥进行测试的方法
- [x] 设计对别人生成的密钥进行测试的方法
- [x] 完成各个角色的测试
	- [x] ClientA(信息交换)
	- [x] ClientB(信息交换)
	- [x] ServerC(秘钥生成与管理)

- docs tree
	- ClientA.py
	- ClientB.py
	- ServerC.py

在本次实验中,`ClientA`和`ClientB`作为客户端,从`ServerC`中请求生成密钥对,在通讯的时候从`ServerC`中获取公钥以进行加密.

- `ClientA`和`ClientB`之间采用socket进行通信,`ServerC`是**静态生成**密钥,单次调用,有能力的话可以添加身份校验功能.当然也可以不使用socket模拟`A` `B`之间的通信
- 使用时需要删除`./keystore`下的秘钥,否则秘钥重复使用会导致初始化失败(当然你也可以删除整个文件夹)

### How to run
1. `rm -r ./keystore`
2. open a new terminal, run `python ClientA.py`
3. open a new terminal, run `python ClientB.py`

Have funs~