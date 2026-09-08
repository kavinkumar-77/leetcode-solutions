# Last updated: 9/8/2026, 1:40:28 PM
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i]=nums[i]**2
        nums.sort()
        return nums