

# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
"""
输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

分析：给定一个字符串变量
得出字符串的变量的位数
逐个比较是否相等
相等则为1，不等则+1
循环
输出count数
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st={}
        x=0
        j=0
        for i in range(len(s)):
            if(s[i] in st):
                j=max(st[s[i]]+1,j)
            x=max(x,i-j+1)
            st[s[i]]=i
        return x

if __name__ == '__main__':
    print(Solution.lengthOfLongestSubstring(1,s='abcd12345ed125ss123456789'))