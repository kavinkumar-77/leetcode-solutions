# Last updated: 7/29/2026, 2:23:02 PM
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # s=set(nums)
        # for i in range(0,len(nums)+1):
        #     if i not in s:
        #         return i
        n=len(nums)
        s1=sum(nums)
        s2=(n*(n+1))//2
        return s2-s1