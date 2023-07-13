# -*- coding: utf-8 -*-
# @Time    : 2023/7/13 17:35
# @Author  : rainbowzhouj
# @FileName: 字典与json互转.py
# @Software: PyCharm

"在Python中使用dumps方法将dict对象转为Json对象，使用loads方法可以将Json对象转为dict对象"
import json

dic={'a':123,'b':'456','c':'rainbow'}
a=json.dumps(dic)
print(a)
b=json.loads(a)
print(b)

dic_str = json.loads(str(dic).replace("'", "\""))
print(dic_str)
"""
下面我解释下上面代码是测试什么:
首先json.loads(jsonstr)这里面的参数只能是jsonstr格式的字符串.当我们使用str将字典dic转化为字符串以后，
得到的结果为: "{'a': 123, 'b': '456', 'c': 'liming'}"。如果直接使用json.loads(str(dic))你会发现出现错误，
原因就是，单引号的字符串不符合Json的标准格式所以再次使用了replace("'", "\"")。得到字典
其实这个例子主要目的是告诉大家Json的标准格式是不支持单引号型字符串的，否则会出现以下错误。
json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes: line 1 column2(char1)
"""