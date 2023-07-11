# -*- coding: utf-8 -*-
# @Time    : 2022/8/12 5:30 下午
# @Author  : rainbowzhouj
# @FileName: 打乱数组.py
# @Software: PyCharm
"""
给你一个整数数组 nums ，设计算法来打乱一个没有重复元素的数组。打乱后，数组的所有排列应该是 等可能 的。

实现 Solution class:

Solution(int[] nums) 使用整数数组 nums 初始化对象
int[] reset() 重设数组到它的初始状态并返回
int[] shuffle() 返回数组随机打乱后的结果
"""
from random import random
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.list = nums


    def reset(self) -> List[int]:
        return self.list


    def shuffle(self) -> List[int]:
        copy_list = self.list[:]
        random.shuffle(copy_list)
        return copy_list

