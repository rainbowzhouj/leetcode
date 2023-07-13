# -*- coding: utf-8 -*-
# @Time    : 2023/7/13 17:43
# @Author  : rainbowzhouj
# @FileName: isuper.py
# @Software: PyCharm
"计算一个文件中的大写字母数量"
with open("A.txt") as f:
    f1=f.readline()
    count=0
    for i in f1:
        if i.isupper(): #isupper()为判断大写字母的方法
            count+=1
print(count)
