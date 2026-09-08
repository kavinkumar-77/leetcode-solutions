# Last updated: 9/8/2026, 1:40:40 PM
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        left_max=nums[0]
        seen_max=nums[0]
        left_size=0
        for i in range(1,len(nums)):
            seen_max=max(seen_max,nums[i])
            if nums[i]<left_max:
                left_size=i
                left_max=seen_max
        return left_size+1