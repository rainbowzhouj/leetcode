# -*- coding: utf-8 -*-
# @Time    : 2022/3/6 2:32 下午
# @Author  : rainbowzhouj
# @FileName: 回文链表.py
# @Software: PyCharm
class Solution:
    def isPalindrome(self,head:ListNode)->bool:
        arr=[]
        while head:
            arr.append(head.val)
            head=head.next
        left,right=0,len(arr)-1
        while left<right:
            if arr[left]!=arr[right]: 
                return False
            else:
                left+=1
                right-=1
        return True
