class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen={}
        if len(nums)==2:
            if nums[0]+nums[1]==target:
                return 0,1
        for i,num in enumerate(nums):
            diff=target-num
            if diff in seen:
                return [seen[diff],i]
            seen[num]=i
