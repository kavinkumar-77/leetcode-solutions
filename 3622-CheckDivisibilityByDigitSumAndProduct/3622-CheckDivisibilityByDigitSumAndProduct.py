# Last updated: 9/8/2026, 1:40:12 PM
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s=str(n)
        ds=0
        dp=1
        for i in range(len(s)):
            ds+=int(s[i])
            dp=dp*int(s[i])
        if n%(ds+dp)==0:
            return True
        else:
            return False


