# Last updated: 7/29/2026, 2:23:00 PM
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if nums[i]==0:
                temp=nums.pop(i)
                nums.insert(n,temp)