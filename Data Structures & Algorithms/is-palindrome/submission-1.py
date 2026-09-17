class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ""
        for i in s:
            if i.isalnum():
                t += i.lower()
        n = len (t)
        for i in range (n):
            if t[i] != t[n-1-i]:
                return False
                
        return True
