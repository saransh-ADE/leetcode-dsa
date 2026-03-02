"""
LeetCode #13 – Roman to Integer
Category: Strings
Difficulty: Easy
Approach: Right-to-left traversal with subtraction rule
Time: O(n)
Space: O(1)
"""

class Solution:
    def romanToInt(self, s: str) -> int:

        roman = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        result =0
        prev=0

        for i in s[::-1]:
            curr=roman[i]
            if curr>=prev:
                result+=curr
            else:
                result-=curr
            prev=curr
        
        return result
        
