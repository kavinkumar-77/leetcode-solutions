# Last updated: 9/8/2026, 1:40:57 PM
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hs={}
        for i,num in enumerate(nums):
            if num in hs:
                hs[num]=hs.get(num)+1
            else:
                hs[num]=1
        res=[]
        for key,value in hs.items():
            if value>1:
                res.append(key)
        return res