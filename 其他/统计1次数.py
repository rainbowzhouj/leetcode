# -*- coding: utf-8 -*-
# @Time    : 2023/7/11 16:39
# @Author  : rainbowzhouj
# @FileName: 统计1次数.py
# @Software: PyCharm

def count_num(n):
    count=[0]*(n+1)
    for i in range (1,n+1):
        s=str(i)
        for c in s:
            if c=='1':
                count[i]+=1
    return sum(count)

if __name__ == '__main__':
    n=12
    print(count_num(n))

