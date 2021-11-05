# -*- coding: utf-8 -*-
# @Time    : 2021/11/5 1:41 下午
# @Author  : rainbowzhouj
# @FileName: 有效的数独.py
# @Software: PyCharm
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        m = len(board[0])
        row = [[] * 9 for _ in range(9)]
        col = [[] * 9 for _ in range(9)]
        nine = [[] * 9 for _ in range(9)]
        for i in range(n):
            for j in range(m):
                tmp = board[i][j]
                if not tmp.isdigit():
                    continue
                if tmp in row[i]:
                    return False
                if tmp in col[j]:
                    return False
                if tmp in nine[(j // 3) * 3 + (i // 3)]:
                    return False
                row[i].append(tmp)
                col[j].append(tmp)
                nine[(j // 3) * 3 + (i // 3)].append(tmp)
        return True
