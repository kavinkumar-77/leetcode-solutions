# Last updated: 7/27/2026, 3:48:20 PM
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for s in strs:
            ss="".join(sorted(s))
            res[ss].append(s)
        return list(res.values())