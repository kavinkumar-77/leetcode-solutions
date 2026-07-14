# Last updated: 7/14/2026, 1:54:45 PM
class Solution:
    def mySqrt(self, x: int) -> int:
        s=x
        while (s*s>x):
            s=(s+x//s) // 2
        return s