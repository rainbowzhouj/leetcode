# -*- coding: utf-8 -*-
# @Time    : 2022/8/2 6:00 下午
# @Author  : rainbowzhouj
# @FileName: 对称二叉树.py
# @Software: PyCharm
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self,root:Optional[TreeNode])->bool:
        def foo(left:TreeNode,right:TreeNode):
            if not left and not right:
                # 如果左右都为空，则返回真
                return True
            if not left or not right:
                # 如果左右只有一个为空，返回假
                return False
            if left.val != right.val:
                # 如果左右值不等，返回假
                return False
            return foo(left.left,right.right) and (left.right,right.left)
        return foo(root.left,root.right)