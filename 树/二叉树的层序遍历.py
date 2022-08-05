# -*- coding: utf-8 -*-
# @Time    : 2022/8/5 3:09 下午
# @Author  : rainbowzhouj
# @FileName: 二叉树的层序遍历.py
# @Software: PyCharm
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue=[root]
        res=[]
        while queue:
            length=len(queue)
            sub_list=[]
            for i in range(length):
                node=queue.pop(0)
                sub_list.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(sub_list)
        return res
