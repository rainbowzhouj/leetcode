#
# def aaa(b ，c):
#     a=len(b)
#     int c
#     for i in range(0,a):
#         j=a-i
#         if c-b[i]==b[j]:
#             return {i,j}
from typing import List


class Solution:
    def twoSum(nums: List[int], target: int) -> List[int]:
        hashmap={}
        for ind,num in enumerate(nums):
            hashmap[num] = ind
        for i,num in enumerate(nums):
            j = hashmap.get(target - num)
            if j is not None and i!=j:
                return [i,j]



if __name__ == '__main__':
    bb=[1,2,3]
    cc=5
    print(Solution.twoSum(bb,cc))
