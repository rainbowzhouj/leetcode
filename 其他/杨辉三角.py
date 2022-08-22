# -*- coding: utf-8 -*-
# @Time    : 2022/8/21 9:52 下午
# @Author  : rainbowzhouj
# @FileName: 杨辉三角.py
# @Software: PyCharm
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        re = []
        for i in range(0, numRows):
            temp = [1] * (i + 1)
            for j in range(0, i + 1):
                if j == 0 or j == i:
                    continue
                temp[j] = re[i - 1][j - 1] + re[i - 1][j]
            re.append(temp)
        return re
