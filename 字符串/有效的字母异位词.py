# -*- coding: utf-8 -*-
# @Time    : 2021/11/11 11:29 上午
# @Author  : rainbowzhouj
# @FileName: 有效的字母异位词.py
# @Software: PyCharm
import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        将s与t 放到两个字典中，key为每个字母，value为每个字母出现的次数
        将字典转化为列表后，比较两个列表中的值是否一样，一样则返回truw
        :param s:
        :param t:
        :return:
        """
        y = {}
        z={}
        while len(s) == len(t):
            for x in s:
                if x not in y:
                    y.update({x: s.count(x)})
            for a in t:
                if a not in z:
                    z.update({a: t.count(a)})
            if y.items() == z.items():
                return True
            else:
                return False
        return False

    def isAnagram1(self, s: str, t: str) -> bool:
        return collections.Counter(s)==collections.Counter(t)

if __name__ == '__main__':
    # s = "anagram"
    # t = "nagaram"
    # print(Solution.isAnagram1(1, s, t))
    z={"a":1,"b":2}
    res="".join(z)
    on=z.keys()
    print(res)
    print(type(res))
    print(on)
    print(type(on))