# -*- coding: utf-8 -*-
# @Time    : 2022/8/19 1:56 下午
# @Author  : rainbowzhouj
# @FileName: 汉明距离.py
# @Software: PyCharm
class Solution:
    def hammingDistance(self,x:int,y:int)->int:
        # 之所以从第三位开始计数，因为二进制字符串为0bxx。
        return bin(x^y)[2:].count("1")