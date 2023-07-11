# -*- coding: utf-8 -*-
# @Time    : 2022/7/7 8:31 下午
# @Author  : rainbowzhouj
# @FileName: 最长公共子串.py
# @Software: PyCharm
# 两个字符串的，最大公共子串

def twoString(a: str, b: str):
    left = 0
    res = ""
    for right in range(len(a) + 1):
        sub = a[right - left:right]
        if sub in b:
            res = sub
            left += 1
    return res


def LCS(str1, str2):
    m = len(str1)
    n = len(str2)
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    pos = 0
    max_len = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    pos = i - 1
    res = str1[pos - max_len + 1:pos + 1]
    return res


if __name__ == '__main__':
    print(twoString("hello", "eell"))
