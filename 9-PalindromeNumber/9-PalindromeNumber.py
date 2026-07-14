# Last updated: 7/14/2026, 1:55:00 PM
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x)
        return(s==s[::-1])
        