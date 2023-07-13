# -*- coding: utf-8 -*-
# @Time    : 2023/7/13 17:02
# @Author  : rainbowzhouj
# @FileName: 文件合并.py
# @Software: PyCharm
"""
有两个磁盘文件A和B，各存放一行字母，要求把这两个文件中的信息合并(按字母顺序排列)，输出到一个新文件C中。
    # 文件 A.txt 内容为 ASDCF
    # 文件 B.txt 内容为 EFGGTG
"""
def file():
    with open("./A.txt") as f1:
        f1_txt=f1.readline()
    with open("./B.txt") as f2:
        f2_txt=f2.readline()
    f3_txt=f1_txt+f2_txt
    f3_list=sorted(f3_txt)
    with open("C.txt","a+")as f3:
        f3.write("".join(f3_list))


## 则预期结果为ACDEFFGGGST
if __name__ == '__main__':
    file()