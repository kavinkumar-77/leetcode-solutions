# Last updated: 8/22/2026, 11:58:27 AM
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


