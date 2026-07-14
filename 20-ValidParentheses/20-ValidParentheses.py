# Last updated: 7/14/2026, 1:54:55 PM
class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map={')':'(',']':'[','}':'{'}
        stack=[]
        for char in s:
            if char in bracket_map:
                if not stack:
                    return False
                top_element=stack.pop()
                if bracket_map[char]!=top_element:
                    return False
            else:
                stack.append(char)
        return len(stack)==0 