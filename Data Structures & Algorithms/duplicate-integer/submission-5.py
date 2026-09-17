class Solution:
    def hasDuplicate(self, x):
        dupl = set()
        for i in x:
            if i in dupl:
                return True
            dupl.add(i)
        return False