# -*- coding: utf-8 -*-
"""
Inference of simple PoW
Author: Hatuw
"""
import warnings
import hashlib

# define
d = 1 # difficulty: 以16进制位表示的前缀0的个数
v = r"1515300020" # 你的学号或姓名
x = 1

if d >= 5:
    warnings.warn("d>=5 may take a long time to compute")

SHR = lambda h, k: hex(h >> k) # 对无符号数h右移k位

sha1 = hashlib.sha1()
sha1.update(v.encode(encoding='utf-8'))

init = bin(int(sha1.hexdigest(), 16))
n = len(init)

target = SHR(2**n-1, d*4)
target_10 = int(target,16)
print("Target: < {}".format(target))

while True:
    sha1.update((v+str(x)).encode(encoding='utf-8'))
    br_val = hex(int(sha1.hexdigest(), 16))
    if int(br_val, 16) < target_10:
        print("v||x: {} || {}".format(v, x))
        print("x is: {}; Hex_val: {}".format(x, br_val))
        break
    x += 1
