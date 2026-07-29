# Last updated: 7/29/2026, 2:23:10 PM
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hs=defaultdict(int)
        n=len(nums)
        for num in nums:
            if num in hs:
                hs[num]+=1
            else:
                hs[num]=1
        for key,value in hs.items():
            if value>(n/2):
                return key