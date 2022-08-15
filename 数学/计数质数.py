# -*- coding: utf-8 -*-
# @Time    : 2022/8/15 9:42 上午
# @Author  : rainbowzhouj
# @FileName: 计数质数.py
# @Software: PyCharm
class Solution:
    def countPrimes(self,n:int)->int:
        isNumPrimes=[True]*n
        count=0
        for i in range(2,n):
            if isNumPrimes[i]:
                count+=1
                for j in range(i*i,n,i):
                    isNumPrimes[j]=False
        return count

s=Solution()
print(s.countPrimes(10))