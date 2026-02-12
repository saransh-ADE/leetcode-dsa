# LeetCode #26 – Remove Duplicates from Sorted Array
# Category: Arrays
# Difficulty: Easy
# Approach: Two Pointers (slow-fast)
# Time: O(n)
# Space: O(1)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        i=0 #slow pointer

        for j in range(1,len(nums)): #fast pointer
            if nums[j]!=nums[i]:
                i+=1
                nums[i]=nums[j]


        return i+1
