# -*- coding: utf-8 -*-
# @Time    : 2023/7/13 17:16
# @Author  : rainbowzhouj
# @FileName: 日期变化.py
# @Software: PyCharm
"""
如果当前的日期为20190530，要求写一个函数输出N天后的日期，(比如 N 为 2，则输出 20190601)
"""
import datetime

"""
获取当前时间
获取指定天数后的新日期
转换为指定的输出格式
"""
def datetime_operate(n:int):
    now=datetime.datetime.now()
    _new_date=now+datetime.timedelta(days=n)
    new_date=_new_date.strftime("%Y%m%d")
    return new_date

if __name__ == '__main__':
    print(datetime_operate(4))