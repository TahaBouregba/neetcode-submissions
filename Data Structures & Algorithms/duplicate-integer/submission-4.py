class Solution:
    def hasDuplicate(self, x):
        seen = set()
        for i in x:
            if i in seen:
                return True
            seen.add(i)
        return False
