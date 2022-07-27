# -*- coding: utf-8 -*-
# @Time    : 2022/7/27 2:29 下午
# @Author  : rainbowzhouj
# @FileName: 二叉树最大深度.py
# @Software: PyCharm
"""
给定一个二叉树，找出其最大深度
"""
class Solution:
    def maxDepth(self,root):
        if root ==None:
            return 0
        left=self.maxDepth(root.left)
        right=self.maxDepth(root.right)
        return max(left,right)+1