# Last updated: 7/14/2026, 1:54:23 PM
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        total=0
        for i in range(0,len(nums),2):
            total=total+nums[i]
        return total