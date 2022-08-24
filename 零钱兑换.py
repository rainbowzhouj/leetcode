# -*- coding: utf-8 -*-
# @Time    : 2022/8/24 10:46 上午
# @Author  : rainbowzhouj
# @FileName: 零钱兑换.py
# @Software: PyCharm
"""
给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。
你可以认为每种硬币的数量是无限的。
"""
import functools
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @functools.lru_cache(amount)
        def dp(rem)->int:
            if rem<0:return -1
            if rem==0:return 0
            mini=int(1e9)
            for coin in self.coins:
                res=dp(rem-coin)
                if res>=0 and res<mini:
                    mini=res+1
            return mini if mini<int(1e9) else -1
        self.coins=coins
        if amount<1:return 0
        return dp(amount)


