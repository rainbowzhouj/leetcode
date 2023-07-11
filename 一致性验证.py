# -*- coding: utf-8 -*-
# @Time    : 2022/8/4 4:04 下午
# @Author  : rainbowzhouj
# @FileName: 一致性验证.py
# @Software: PyCharm
"""
1、通过脚本的方式连接hive/ES。进行查询hive/ES中的数据
2、比较Hive和ES的数据条数，是否一致
"""
import os
from pyhive import hive


def main():
    conn = hive.Connection(
        host='10.25.19.30',
        port=10000,
        username='hadoop',
        database='default',
        auth='NOSASL'
    )

    cursor = conn.cursor()
    cursor.execute('show databases')
    res = cursor.fetchall()
    for x in res:
        print(x)
    conn.close()


# 查询Hive中的数据
def monitor_hive_data(data_date):
    hive_user = "select count(1) from dw.userprofile_userlabel_map_all where data_date='{}' ".format(data_date)
    user_count = os.popen("hive -S -e \"" + hive_user + "\"").read().strip()
    return user_count


# 查询es中的数据
def monitor_es_data(data_date):
    userid_search = "curl http://10.25.19.30:9200_cat/count/" + data_date + "_userid/"
    userid_num = str(os.popen(userid_search).read()).split('')[-1].strip()
    return userid_num


def update_es_data(data_date):
    '''
    data_date: 查询数据日期
    '''
    esdata = monitor_es_data(data_date)  # 查询es中的数据
    hivedata = monitor_hive_data(data_date)  # 查询Hive中的数据
    print("esdata ======>{}".format(esdata))
    print("hivedata ======>{}".format(hivedata))
    assert esdata[0] == hivedata[0]


if __name__ == "__main__":
    main()
