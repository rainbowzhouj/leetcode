# -*- coding: utf-8 -*-
# @Time    : 2021/11/19 10:51 上午
# @Author  : rainbowzhouj
# @FileName: 最长公共前缀.py
# @Software: PyCharm
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) == 0: return ""
        pre = strs[0]
        strs = strs[1:]
        for i in range(len(strs)):
            count = 0
            if len(pre) < len(strs[i]):
                length = len(pre)
            else:
                length = len(strs[i])
            for j in range(length):
                if strs[i][j] == pre[j]:
                    count += 1
                else:
                    break
            pre = pre[:count]
        return pre

if __name__ == '__main__':
    strs = ["flower", "low"]
    print(Solution.longestCommonPrefix(1, strs))
    # s="【卓越好课节】3＋1卓越方法课-剑桥高材生们都在用的『康奈尔笔记法』，让你学习知识轻松又快乐！（初一至高三）"
    # print(len(s))

    """
    # 找出 2022年订单金额大于1的所有客户,在2022年按天级别的订单消费情况
    select 订单id from 订单表 where  会员id=(
    select distinct 会员id from 订单表 where 订单金额 > 100 and datatime 
    )  and order_by datatime between dateadd(DAY,-365,2022-12-31);
    
    SELECT account_id,create_time FROM facebook_ads_insights WHERE account_id=(
SELECT account_id FROM facebook_ads_insights WHERE spend>1 AND YEAR(create_time)=2022 )
GROUP BY create_time BETWEEN '2022-01-01' and '2022-12-31';

    """

