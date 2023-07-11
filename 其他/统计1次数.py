# -*- coding: utf-8 -*-
# @Time    : 2023/7/11 16:39
# @Author  : rainbowzhouj
# @FileName: 统计1次数.py
# @Software: PyCharm

def count_one(n):
  # 初始化一个数组count，长度为n+1，初始值为0
  count = [0] * (n + 1)
  # 遍历从1到n的每个整数i
  for i in range(1, n + 1):
    # 将i转换为字符串s
    s = str(i)
    # 遍历s中的每个字符c
    for c in s:
      # 如果c等于'1'，则将count[i]加一
      if c == '1':
        count[i] += 1
  # 返回count数组中所有元素的和
  return sum(count)

if __name__ == '__main__':
    n=12
    print(count_one(n))

