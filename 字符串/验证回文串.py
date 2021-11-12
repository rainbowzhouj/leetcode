# -*- coding: utf-8 -*-
# @Time    : 2021/11/12 11:06 上午
# @Author  : rainbowzhouj
# @FileName: 验证回文串.py
# @Software: PyCharm
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)==0:
            return True
        new=s.lower()
        res=''.join([x for x in new if x.isalpha() or x.isdigit()])
        y=len(res)
        for i in range(y//2) :
            if res[i]!=res[y-i-1]:
                return False
        return True

if __name__ == '__main__':
    s1="A man, a plan, a canal: Panam"
    print(Solution.isPalindrome(1, s1))