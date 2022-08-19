# -*- coding: utf-8 -*-
# @Time    : 2022/8/19 1:45 下午
# @Author  : rainbowzhouj
# @FileName: 位1的个数.py
# @Software: PyCharm


class Solution:
    def hammingWeight(self,n:int)->int:
        return bin(n).count("1") # 使用python特性 bin(3)=ob11
    def hammingWeight1(self,n:int)->int:
        res=0
        while n:
            res+=n&1 #res+=(n&1) 11&1=1,10&1=0 比较最后一位相同1，不同0
            n>>=1
        return res

s=Solution()
print(s.hammingWeight1(11111111111111111111111111111101))