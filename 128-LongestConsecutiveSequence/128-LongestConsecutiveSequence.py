# Last updated: 7/14/2026, 1:54:38 PM
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_len=0
        nums_set=set(nums)
        for num in nums_set:
            if num-1 not in nums_set:
                current=num
                current_len=1
                while current+1 in nums_set:
                    current+=1
                    current_len+=1
                max_len=max(max_len,current_len)
        return max_len