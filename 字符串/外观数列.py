# -*- coding: utf-8 -*-
# @Time    : 2021/11/18 4:52 下午
# @Author  : rainbowzhouj
# @FileName: 外观数列.py
# @Software: PyCharm
class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return '1'
        cas=self.countAndSay(n-1)
        cas_new=''
        i=0
        j=1
        cas=='0'
        while(j<len(cas)):
            if cas[i]!=cas[j]:
                cas_new+=str(j-i)+str(cas[i])
                i=j
            j+=1
        return cas_new