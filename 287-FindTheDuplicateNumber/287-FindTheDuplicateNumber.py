# Last updated: 9/8/2026, 1:41:07 PM
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hs={}
        for i in range(len(nums)):
            if nums[i] in hs:
                hs[nums[i]]=hs.get(nums[i])+1
            else:
                hs[nums[i]]=1
        for key,value in hs.items():
            if value>1:
                return key