# -*- coding: utf-8 -*-
# @Time    : 2023/7/13 17:54
# @Author  : rainbowzhouj
# @FileName: Connection_Mysql.py
# @Software: PyCharm

import mysql.connector

# 连接数据库
conn = mysql.connector.connect(
  host='localhost',
  user='root',
  password='password',
  database='mydb'
)

# 获取游标
cursor = conn.cursor()

# 编写SQL查询语句
sql = 'SELECT * FROM users'

# 执行SQL语句
cursor.execute(sql)

# 获取查询结果
results = cursor.fetchall()

# 遍历并打印结果
for result in results:
  print(result)

# 关闭游标和连接
cursor.close()
conn.close()