# Last updated: 7/14/2026, 1:54:33 PM
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        no=0
        k=k%n
        for i in range(k):
            no=nums.pop()
            nums.insert(0,no)            

        