# 实验二 Hash算法实验

整体完成情况:

- [x] 构造谜题并求解


## Requirement

*This repo has two inference, C++ and Python. The following requirement is just for the Python's inference.*

- Ubuntu16.04.4 LTS

## 实验要求

- Tips
    - HASH(m)：表示对消息串进行哈希计算；
    - n：哈希函数值的长度，要求至少为160比特；
    - d：以16进制位表示的前缀0的个数；
    - SHR(h, k)：对无符号数h右移k位；
    - v||x：两个字符串首尾相连


- 构造谜题并求解

    1. d = 1
    2. v = < Your name > / < Your ID >
    3. Find x: Hash(v||x) < SHR(2^n-1, d*4)
    4. Store x
    5. d = 2, 3...; repeat (1)--(4)

- Analyse the result
