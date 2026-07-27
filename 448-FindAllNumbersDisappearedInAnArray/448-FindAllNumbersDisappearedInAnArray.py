# Last updated: 7/27/2026, 3:48:05 PM
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result=[]
        arr=set(nums)
        for i in range(1,len(nums)+1):
            if i not in arr:
                result.append(i)
        return result