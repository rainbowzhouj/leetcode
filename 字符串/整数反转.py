# -*- coding: utf-8 -*-
# @Time    : 2021/11/9 12:28 下午
# @Author  : rainbowzhouj
# @FileName: 整数反转.py
# @Software: PyCharm
class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        if s[0] == '-':
            s_rev = s[0] + s[-1:-len(s):-1]
        else:
            s_rev = s[::-1]
        x_rev = int(s_rev)
        if -2 ** 31 <= x_rev <= 2 ** 31 - 1:
            return x_rev
        return 0



if __name__ == '__main__':
    n=120
    print(Solution.reverse(1, n))

