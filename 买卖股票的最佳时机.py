# -*- coding: utf-8 -*-
# @Time    : 2021/10/28 2:06 下午
# @Author  : rainbowzhouj
# @FileName: 买卖股票的最佳时机.py
# @Software: PyCharm
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total=0
        for i in range(len(prices)-1 ):
            if prices[i+1]>prices[i]:
                total=total+prices[i+1]-prices[i]
        return total

    def best(self,prices: List[int])->int:
        return sum([prices[i+1]-prices[i] for i in range(len(prices)-1) if prices[i+1]>prices[i]])

if __name__ == '__main__':
    a=[7,1,3,5,6]
    b=[2,1]
    print(Solution.maxProfit(a, a))
    print(Solution.best(a, b))