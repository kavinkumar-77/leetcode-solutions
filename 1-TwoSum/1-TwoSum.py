# Last updated: 7/14/2026, 1:55:06 PM
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen_nums={}
        for i,num in enumerate(nums):
            complement = target-num
            if complement in seen_nums:
                return [seen_nums[complement],i]
            else:
                seen_nums[num]=i
