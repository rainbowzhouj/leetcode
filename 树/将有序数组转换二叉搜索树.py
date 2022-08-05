# -*- coding: utf-8 -*-
# @Time    : 2022/8/5 8:24 下午
# @Author  : rainbowzhouj
# @FileName: 将有序数组转换二叉搜索树.py
# @Software: PyCharm
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        mid = len(nums)//2
        root = TreeNode(nums[mid])
        root.left = Solution.sortedArrayToBST(self,nums[:mid])
        root.right =  Solution.sortedArrayToBST(self,nums[mid+1:])
        return root