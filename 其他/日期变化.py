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

def time_diff():
    # 获取当前的日期和时间
    now = datetime.datetime.now()
    # 获取 7 月 1 号零点的日期和时间
    start = datetime.datetime(now.year, 7, 1, 0, 0, 0)
    diff = now - start
    # 将 timedelta 对象转换为秒数
    seconds = diff.total_seconds()
    # 将秒数转换为周、天、小时、分钟、秒数
    weeks = int(seconds // (7 * 24 * 3600))
    # days = int((seconds % (7 * 24 * 3600)) // (24 * 3600))
    # hours = int((seconds % (24 * 3600)) // 3600)
    # minutes = int((seconds % 3600) // 60)
    # seconds = int(seconds % 60)
    weeks, seconds = divmod(seconds, (7 * 24 * 3600))
    days, seconds = divmod(seconds, (24 * 3600))
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    seconds = int(seconds)

    # 打印输出结果
    print(f"从7月1号零点到现在共花费了{weeks}周{days}天{hours}小时{minutes}分{seconds}秒。")


if __name__ == '__main__':
    # print(datetime_operate(4))
    time_diff()
