# Last updated: 9/8/2026, 1:42:07 PM
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        max_len=0
        left=0
        s1=set()
        for right in range(len(s)):
            while s[right] in s1:
                s1.remove(s[left])
                left+=1
            s1.add(s[right])
            c_len=len(s1)
            max_len=max(max_len,c_len)
        return max_len