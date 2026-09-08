# Last updated: 9/8/2026, 1:40:32 PM
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