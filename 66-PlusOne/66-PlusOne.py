# Last updated: 7/14/2026, 1:54:47 PM
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num_str=''.join(map(str,digits))
        num=int(num_str)
        inc_num=num+1
        results=[int(digit) for digit in str(inc_num)]
        return results