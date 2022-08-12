# -*- coding: utf-8 -*-
# @Time    : 2021/10/28 2:06 下午
# @Author  : rainbowzhouj
# @FileName: 买卖股票的最佳时机.py
# @Software: PyCharm
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # total=0
        # for i in range(len(prices)-1 ):
        #     if prices[i+1]>prices[i]:
        #         total=total+prices[i+1]-prices[i]
        # return total
        r = 0
        min_price = float('inf')  # float('inf')表示负无穷
        for price in prices:
            min_price = min(min_price, price)  # 截止到当前的最低价（买入价）
            r = max(r, price - min_price)  # 截止到目前的最高利润
        return r


    def best(self,prices: List[int])->int:
        return sum([prices[i+1]-prices[i] for i in range(len(prices)-1) if prices[i+1]>prices[i]])

s=Solution()
a=[7,1,3,5,6]
b=[2,1]
print(s.maxProfit(a))
print(s.best(a))