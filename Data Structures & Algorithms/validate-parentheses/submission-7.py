        
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close = {")":"(" , "]":"[" , "}" : "{"}
        for i in s :
            if i not in close:
                stack.append(i)
            elif not stack or stack[-1] != close[i]:
                return False
            else:
                stack.pop()
        return stack == []
            


