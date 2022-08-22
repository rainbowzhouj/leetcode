# -*- coding: utf-8 -*-
# @Time    : 2022/8/21 9:51 下午
# @Author  : rainbowzhouj
# @FileName: 颠倒二进制位.py
# @Software: PyCharm
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            res <<= 1  # 新增一位
            res += n & 1  # 取出来最后一位，并加到res
            n >>= 1  # 去除最后一位
        return res