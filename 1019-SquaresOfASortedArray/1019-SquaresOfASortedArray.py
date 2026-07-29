# Last updated: 7/29/2026, 2:22:54 PM
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i]=nums[i]**2
        nums.sort()
        return nums