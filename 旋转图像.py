# -*- coding: utf-8 -*-
# @Time    : 2021/11/8 11:05 上午
# @Author  : rainbowzhouj
# @FileName: 旋转图像.py
# @Software: PyCharm
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        旋转90度，可视作为先上下对折，然后45度角对折
        """
        n=len(matrix)
        # 上下交换
        for i in range(n//2):
            matrix[i],matrix[n-i-1]=matrix[n-i-1],matrix[i]
        # 对角线交换
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        return matrix



if __name__ == '__main__':
    matrix1 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    print(Solution.rotate(1, matrix1))