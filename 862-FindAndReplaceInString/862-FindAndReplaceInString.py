# Last updated: 8/22/2026, 11:59:30 AM
class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        v_r={}
        for index,source,target in zip(indices,sources,targets):
            if s.startswith(source,index):
                v_r[index]=(source,target)
        result=[]
        ci=0
        n=len(s)
        while ci<n:
            if ci in v_r:
                source,target=v_r[ci]
                result.append(target)
                ci+=len(source)
            else:
                result.append(s[ci])
                ci+=1
        return "".join(result)