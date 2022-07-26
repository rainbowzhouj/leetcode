# -*- coding: utf-8 -*-
# @Time    : 2022/7/26 10:56 上午
# @Author  : rainbowzhouj
# @FileName: 环形链表.py
# @Software: PyCharm
from typing import Optional


class ListNode:
    pass


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashmap=set()
        while head:
            if head in hashmap:
                return True
            hashmap.add(head)
            head=head.next
        return False

if __name__ == '__main__':
    print(Solution.hasCycle([3,2,0,-4]))