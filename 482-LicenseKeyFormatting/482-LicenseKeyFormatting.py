# Last updated: 7/14/2026, 1:54:24 PM
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        cleaned=s.replace("-","").upper()
        fgs=len(cleaned)%k
        groups=[]
        if fgs>0:
            groups.append(cleaned[:fgs])
        for i in range(fgs,len(cleaned),k):
            groups.append(cleaned[i:i+k])
        return "-".join(groups)