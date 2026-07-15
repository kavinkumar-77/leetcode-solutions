# Last updated: 7/15/2026, 11:13:15 AM
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]