# Last updated: 7/14/2026, 1:54:20 PM
class Solution(object):
    def concatWithReverse(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return nums+nums[::-1]