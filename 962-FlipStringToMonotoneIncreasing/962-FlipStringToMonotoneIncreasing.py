# Last updated: 8/22/2026, 11:59:13 AM
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        res=0
        cnt=0
        for c in s:
            if c=="1":
                cnt+=1
            else:
                res=min(res+1,cnt)
        return res