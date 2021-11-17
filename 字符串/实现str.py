# -*- coding: utf-8 -*-
# @Time    : 2021/11/17 10:58 上午
# @Author  : rainbowzhouj
# @FileName: 实现str.py
# @Software: PyCharm
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n=len(haystack)
        left=0
        right=len(needle)
        if right==0:
            return 0
        while right<=n:
            if haystack[left:right]==needle:
                return left
            left+=1
            right+=1
        return -1

if __name__ == '__main__':
    print(Solution.strStr(1,"hello", "ll"))
