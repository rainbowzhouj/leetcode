from typing import List

"""
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

"""
class Solution:
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        m=[]
        i=0
        j=1
        while target!=nums[i]+nums[j] :
            if j==n-1:
                i+=1
                j=i
            else:
                j+=1


    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        m=[]
        for i in range(n-1):
            for j in range(n):
                if i!=j and target==nums[i]+nums[j]:
                    m.append(i)
                    m.append(j)
                    return m

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        dcit = {}
        for i in range(len(nums)):
            if target - nums[i] in dcit:
                return [dcit[target - nums[i]], i]
            dcit[nums[i]] = i
        return []



if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 19
    print(Solution.twoSum2(1,nums, target))


#a=Solution.addTwoNumbers()

