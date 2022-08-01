# -*- coding: utf-8 -*-
# @Time    : 2022/8/1 11:30 下午
# @Author  : rainbowzhouj
# @FileName: 验证二叉搜索树.py
# @Software: PyCharm

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #递归并引入上界，下界来判断是否有效的二叉搜索树
        def check(node, min_val = float('-inf'), max_val = float('inf')) -> bool:
            if not node:
                return True
            #每个节点如果超过这个范围，直接返回false
            if node.val <= min_val or node.val >= max_val:
                return False
            #这里再分别以左右两个子节点分别判断，
            #左子树范围的最小值是minVal，最大值是当前节点的值，也就是root的值，因为左子树的值要比当前节点小
            #右子数范围的最大值是maxVal，最小值是当前节点的值，也就是root的值，因为右子树的值要比当前节点大
            return check(node.left, min_val, node.val) and check(node.right, node.val, max_val)
        return check(root)

