# -*- coding: utf-8 -*-
# @Time    : 2023/7/11 16:10
# @Author  : rainbowzhouj
# @FileName: 找第二的数.py
# @Software: PyCharm

def find_second_max(data):
  # 初始化最大元素和第二大元素为负无穷
  max = float('-inf')
  second_max = float('-inf')
  # 遍历数组中的每个元素
  for num in data:
    # 如果当前元素大于最大元素，则更新最大元素和第二大元素
    if num > max:
      second_max = max
      max = num
    # 如果当前元素小于最大元素但大于第二大元素，则更新第二大元素
    elif num > second_max:
      second_max = num
  # 返回第二大元素
  return second_max

if __name__ == '__main__':
    data = [3, 5, 1, 7, 9, 4, 6, 8]
    print(find_second_max(data))