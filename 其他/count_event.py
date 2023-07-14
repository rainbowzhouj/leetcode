# -*- coding: utf-8 -*-
# @Time    : 2023/7/14 14:42
# @Author  : rainbowzhouj
# @FileName: count_event.py
# @Software: PyCharm
"""
click|11
show|2
move|4
click|2
move|4
...

每行竖线左边是事件类型，右边是事件出现的次数（事件类型不限于上述几种）。统计每种事件出现的总次数

返回结果：
{"click":13,"show":2,"move":8}
写一个方法，返回一个字典
"""


def count_event(input_str):
    dic = {}  # 定义一个字典
    for line in input_str.strip().split('\n'):  # 对传输的列进行判断,排除异常
        event_type, count = line.strip().split('|')
        if event_type in dic:  # 获取相关列的key
            dic[event_type] += int(count)  # 将对应key的value相加
        else:
            dic[event_type] = int(count)
    return dic  # 返回相应的key和value

def enum(input_str):
    dic = {}
    for s in input_str.split():
        dic[s.split('|')[0]] = dic.get(s.split('|') [0], 0) + int(s.split('|')[1])
    return dic

if __name__ == '__main__':
    input = """click|11
show|2
move|4
click|2
move|4"""
    print(count_event(input))
    print(enum(input))
