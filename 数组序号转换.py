# -*- coding: utf-8 -*-
# @Time    : 2022/7/28 11:10 下午
# @Author  : rainbowzhouj
# @FileName: 数组序号转换.py
# @Software: PyCharm
from typing import List

"""
你一个整数数组 arr ，请你将数组中的每个元素替换为它们排序后的序号。

序号代表了一个元素有多大。序号编号的规则如下：

序号从 1 开始编号。
一个元素越大，那么序号越大。如果两个元素相等，那么它们的序号相同。
每个数字的序号都应该尽可能地小。

"""
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranks = {v: i for i, v in enumerate(sorted(set(arr)), 1)}
        return [ranks[v] for v in arr]

if __name__ == '__main__':
    print(Solution.arrayRankTransform(1,[40,20,10,30]))