# -*- coding: utf-8 -*-
# @Time    : 2022/8/15 9:51 上午
# @Author  : rainbowzhouj
# @FileName: Fizz Buzz.py
# @Software: PyCharm
class Solution:
    def fizzBuzz1(self,n:int)->int:
        l=[]
        for i in range(1,n+1):
            if i%15==0:
                l.append("FizzBuzz")
            elif i%3==0:
                l.append('Fizz')
            elif i%5==0:
                l.append('Buzz')
            else:
                l.append(str(i))
        return l

##方法2，可以通过步长，进行判断，设置不同的起始值，如：起始值为1，2，4，14，步长为1，3，5，15
s=Solution()
print(s.fizzBuzz(15))