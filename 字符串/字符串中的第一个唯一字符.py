# -*- coding: utf-8 -*-
# @Time    : 2021/11/10 2:32 下午
# @Author  : rainbowzhouj
# @FileName: 字符串中的第一个唯一字符.py
# @Software: PyCharm

"""
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
s = "leetcode"
返回 0

s = "loveleetcode"
返回 2

"""
import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        哈希解决，两次遍历
        :param s:
        :return:
        """
        hasp_map = collections.defaultdict(int)
        for num in s:
            hasp_map[num] += 1
        for i in range(len(s)):
            if hasp_map.get(s[i])==1:
                return i
        return -1

    def firstUniqChar1(self, s: str) -> int:
        """
        循环遍历，耗时过长
        :param s:
        :return:
        """
        x=len(s)
        for i in range(x):
            if s.count(s[i]) == 1:
                return s.index(s[i])
        return -1

    def firstUniqChar2(self, s: str) -> int:
        """
        利用find方法，用法：字符串中寻找某个字符的下标，可以限定范围
        利用rfind方法，用法：字符串中倒序寻找莫个字符的下标，可以限定范围
        :param s:
        :return:
        """
        for x in s:
            if s.find(x) == s.rfind(x):
                return s.find(x)
        return -1

    def firstUniqChar3(self, s: str) -> int:
        """
        利用字典法求解，先统计每个字母出现的次数，再找出次数为1的字母对应的下标值
        :param s:
        :return:
        """
        d={}
        for x in s:
            if x not in d:
                d.update({x: s.count(x)})
        for y in d.keys():
            if d[y] == 1:
                return s.index(y)
        return -1




if __name__ == '__main__':

    s='dddccdbba'
    print(s.find("d"),s.rfind("d"))
    print(Solution.firstUniqChar2(1,s))
