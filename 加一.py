# -*- coding: utf-8 -*-
# @Time    : 2021/11/2 10:34 上午
# @Author  : rainbowzhouj
# @FileName: 加一.py
# @Software: PyCharm
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        while (1<= len(digits) and len(digits)<=100):
            for i in range (len(digits)-1,-1,-1):
                if digits[i]!=9 :
                    digits[i]+=1
                    return digits

                else:
                    digits[i]=0
            digits.insert(0,1)
            return digits

if __name__ == '__main__':
    num=[9,8,9]
    num1=[9,9,9]
    print(Solution.plusOne(1,num1))