# -*- coding: utf-8 -*-
# @Time    : 2022/8/23 10:38 上午
# @Author  : rainbowzhouj
# @FileName: 反转链表.py
# @Software: PyCharm
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head;
        r=self.reverseList(head.next)
        head.next.next=head
        head.next=None
        return r

    def reverse(self,head: Optional[ListNode]) -> Optional[ListNode]:
        last_head=None
        while head:
            next=head.next
            head.next=last_head
            last_head=head
            head=next
        return last_head

s=Solution()
head=[1,2]
print(s.reverse(head))


