# -*- coding: utf-8 -*-
# @Time    : 2022/8/17 10:28 上午
# @Author  : rainbowzhouj
# @FileName: 罗马数字转整数.py
# @Software: PyCharm
class Solution:
    def romanToInt(self, s: str) -> int:
        dic={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        ret=0
        for i in range(len(s)-1,-1,-1):
            if ret>4*dic[s[i]]:
                ret-=dic[s[i]]
            else:
                ret+=dic[s[i]]
        return ret