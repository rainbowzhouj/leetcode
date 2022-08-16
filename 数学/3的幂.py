# -*- coding: utf-8 -*-
# @Time    : 2022/8/16 5:49 下午
# @Author  : rainbowzhouj
# @FileName: 3的幂.py
# @Software: PyCharm
class Solution:
    def isPowerofThree(self,n:int)->bool:
        #题中n的范围是-2^31 <= n <= 2^31 - 1，而在这个范围内3的最大幂是1162261467，在比他大就超过int表示的范围了，我们直接用它对n求余即可，过求余的结果是0，说明n是3的幂次方
        return (n>0 and 1162261467 % n == 0)

    def isPowerofThree2(self,n:int)->bool:
        # 一直除以3
        if (n>1):
            while (n%3==0):
                n/=3;
        return n==1;

    def isPowerofThree3(self,n:int)->bool:
        # 递归的方式解决
        return n>0 and (n==1 or (n%3==0 and self.isPowerofThree3(n/3)))

s=Solution()
print(s.isPowerofThree3(9))