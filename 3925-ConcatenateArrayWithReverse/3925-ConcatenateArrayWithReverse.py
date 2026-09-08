# Last updated: 9/8/2026, 1:40:09 PM
class Solution(object):
    def concatWithReverse(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return nums+nums[::-1]