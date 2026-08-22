# Last updated: 8/22/2026, 11:59:53 AM
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        slot=1
        arr=preorder.split(',')
        for num in arr:
            if slot==0:
                return False
            if num=='#':
                slot-=1
            else:
                slot+=1
        return slot==0