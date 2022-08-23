# -*- coding: utf-8 -*-
# @Time    : 2022/3/3 9:40 上午
# @Author  : rainbowzhouj
# @FileName: 合并两个有序链表.py
# @Software: PyCharm
"""
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy=List[0]
        move=dummy
        if list1==None:
            return list2
        if list2==None:
            return list1
        if list1.val<list2.val:
            list1.next=max(list1.next,list2)
            return list1
        else :
            list2.next=max(list1,list2.next)
            return list2

    def mergeTwoLists(self, list1, list2) :
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        is_max = list1.val >= list2.val
        l_max = list1 if is_max else list2
        l_min = list2 if is_max else list1
        while l_min and l_max and l_min.next:
            if l_min.val <= l_max.val <= l_min.next.val:
                l_min.next = ListNode(l_max.val, l_min.next)
                l_max = l_max.next
            l_min = l_min.next
        if l_max is not None:
            l_min.next = l_max
        return list2 if is_max else list1

