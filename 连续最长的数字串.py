# -*- coding: utf-8 -*-
# @Time    : 2022/3/30 5:58 下午
# @Author  : rainbowzhouj
# @FileName: 连续最长的数字串.py
# @Software: PyCharm

# a = input()
# maxLen, curLen, maxStr, curStr = 0, 0, "", ""
#
# for i, v in enumerate(a):
#     if v.isnumeric():
#         curLen += 1
#         curStr += v
#         if curLen >= maxLen:
#             maxLen = curLen
#             maxStr = curStr
#     else:
#         curLen = 0
#         curStr = ""
# print(maxStr)
# print(maxLen)


def add(n,i):
    return n+i

def atest():
    for i in range(4):
        yield i

g = atest()
for n in [1,10]:
    g = (add(n,i) for i in g)
print(list(g))