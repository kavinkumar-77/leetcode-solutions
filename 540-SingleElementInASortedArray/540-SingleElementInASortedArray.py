# Last updated: 7/27/2026, 3:48:03 PM
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        return sum(set(nums))*2 - sum(nums)