class Solution:
    def isAnagram(self , s: str , t: str) -> bool :
        T = sorted(t)
        S = sorted(s)
        return S == T
        


            