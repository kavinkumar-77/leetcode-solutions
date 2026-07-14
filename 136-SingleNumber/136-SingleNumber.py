# Last updated: 7/14/2026, 1:54:37 PM
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result=0
        for num in nums:
            result^=num
        return result