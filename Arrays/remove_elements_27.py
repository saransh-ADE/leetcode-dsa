#Add LeetCode #27 Remove Element using two pointers (O(n) time, O(1) space)

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        n=len(nums)
    
        while i<n:
            if nums[i]==val:
                nums[i]=nums[n-1]
                n=n-1
            else:
                i=i+1
            

        return i
