# -*- coding: utf-8 -*-
# @Time    : 2021/11/19 10:51 上午
# @Author  : rainbowzhouj
# @FileName: 最长公共前缀.py
# @Software: PyCharm
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) == 0: return ""
        pre = strs[0]
        strs = strs[1:]
        for i in range(len(strs)):
            count = 0
            if len(pre) < len(strs[i]):
                length = len(pre)
            else:
                length = len(strs[i])
            for j in range(length):
                if strs[i][j] == pre[j]:
                    count += 1
                else:
                    break
            pre = pre[:count]
        return pre

if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]
    print(Solution.longestCommonPrefix(1, strs))